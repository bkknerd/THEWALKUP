from pathlib import Path
import json,html,re
ROOT=Path(__file__).resolve().parent
load=lambda n:json.loads((ROOT/'content'/n).read_text())
e=lambda x:html.escape(str(x),quote=True)
def url(x):
 if not isinstance(x,str) or not (x.startswith('/') and not x.startswith('//') or x.startswith('https://')):raise ValueError('Invalid URL: '+str(x))
 return e(x)
def js(v):return json.dumps(v,ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
s=load('site.json');M={}
for c in load('menu.json')['categories']:
 groups=[]
 for g in c['groups']:
  its=[]
  for it in g['items']:
   if it.get('subheading'):its.append(['#'+it['name']]);continue
   p=it['price']
   if not isinstance(p,(int,float)) or p<0:raise ValueError('Invalid price')
   its.append([it['name'],p,it.get('description','')])
  groups.append([g['title'],None,its])
 M[c['name']]=groups
R=[[r['name'],r['attribution'],r['quote']] for r in load('reviews.json')['reviews']]
A={}
for a in load('animations.json')['drinks']:
 if a['glass'] not in ['coupe','rocks','highball'] or not re.fullmatch(r'#[0-9a-fA-F]{6}',a['color']) or not a['ingredients']:raise ValueError('Invalid animation')
 A[a['name']]=[a['glass'],a['color'],a['ingredients']]
v={'TITLE':e(s['title']),'LOGO':url(s['logo']),'HERO_IMAGE':url(s['hero_image']),'MENU_JSON':js(M),'REVIEWS_JSON':js(R),'ANIMATIONS_JSON':js(A),'ADDRESS':e(s['address']).replace('\n','<br>'),'FOOTER':e(s['footer'])}
for c in s['copy']:v['COPY_'+c['key']]=e(c['text'])
v['GALLERY']=''.join('<figure class="ph '+['a','b','c','d'][i%4]+'"><div class="fr"><img loading="lazy" decoding="async" src="'+url(g['image'])+'" alt="'+e(g['alt'])+'"></div><figcaption>'+e(g['caption'])+'</figcaption></figure>' for i,g in enumerate(s['gallery']))
v['HOURS']=''.join('<tr data-d="'+e(h['days'])+'"><td>'+e(h['label'])+'</td><td>'+e(h['time'])+'</td></tr>' for h in s['hours'])
v['CONTACTS']='<dt>Phone</dt><dd><a href="tel:'+e(re.sub(r'[^+0-9]','',s['phone']))+'">'+e(s['phone'])+'</a></dd><dt>Email</dt><dd><a href="mailto:'+e(s['email'])+'">'+e(s['email'])+'</a></dd><dt>Seating</dt><dd>'+e(s['seating'])+'</dd><dt>Per person</dt><dd>'+e(s['budget'])+'</dd>'
v['LINKS']=''.join('<a href="'+url(s[k])+'" rel="noopener">'+n+'</a>' for k,n in [('directions','Directions'),('instagram','Instagram'),('facebook','Facebook')])
t=(ROOT/'templates/home.html').read_text().replace('var first=[2,1,5,11]','var first=[2,1,5,11].filter(function(i){return i<R.length})')
for k,x in v.items():t=t.replace('{{'+k+'}}',x)
if re.search(r'\{\{[A-Za-z_]+\}\}',t):raise ValueError('Unresolved homepage placeholder')
(ROOT/'index.html').write_text(t)
c=load('cinema.json');t=(ROOT/'templates/cinema.html').read_text();cards=''.join('<article class="drink"><p class="film">'+e(d['film'])+'</p><h2>'+e(d['name'])+'</h2><p class="note">'+e(d['note'])+'</p><p class="ingredients"><span>Common ingredients</span>'+e(d['ingredients'])+'</p><a class="source" href="'+url(d['source'])+'" target="_blank" rel="noopener noreferrer">Source and context ↗</a></article>' for d in c['drinks'])
for k,x in {'TITLE':e(c['title']),'LOGO':url(s['logo']),'INTRO':e(c['intro']),'NOTICE':e(c['notice']),'CARDS':cards}.items():t=t.replace('{{'+k+'}}',x)
(ROOT/'movie-cocktails/index.html').write_text(t)
print('Built homepage and movie-cocktails page')
