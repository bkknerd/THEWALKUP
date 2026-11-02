# THE WALKUP — ONE FOLDER, READY FOR NETLIFY

## Quick upload (public site)
1. Extract the ZIP.
2. In Netlify, choose Add new project / Deploy manually (or Netlify Drop).
3. Drag the entire `WalkUp-Netlify` FOLDER into the upload area. Its top level contains index.html. Do not upload the ZIP itself or only the HTML file.
4. Open your deployed homepage and `/movie-cocktails/`. All images and navigation are already included. No separate add-on install is required.

Manual upload publishes the prepared static pages. It DOES NOT activate CMS repository authentication or automatic publishing.

## Activate form submissions
Enable Forms > Form detection for the project, then upload/redeploy the same folder again. Test the newsletter and contact forms from the actual HTTPS site. Find each submission in the private Netlify Forms dashboard. Configure submission email notifications with your real recipient address. Account limits and charges may apply; check your plan. Honeypot fields are included. Review privacy wording, consent, retention and spam handling before launch.

`/inbox` is a shortcut to instructions for the Netlify inbox, not a custom publicly accessible submission database. Netlify login protects actual submission data. No secrets, tokens, or submission records belong in this folder. Newsletter forms collect requests; sending campaigns requires a separate email platform connection.

## Activate the CMS at /admin/
1. Create a GitHub repository and commit this folder's CONTENTS to branch main.
2. Edit admin/config.yml: replace YOUR_GITHUB_OWNER/YOUR_REPOSITORY with the real repository.
3. Connect that repository to Netlify. Build: python3 build.py. Publish: . (the repository root). No third-party Python packages are required.
4. Configure GitHub OAuth for Decap CMS using the current instructions at https://decapcms.org/docs/github-backend/ and Netlify's authentication-provider settings. Use the callback URL provided by that setup. Never publish your OAuth secret or access token.
5. Open /admin/, sign in with GitHub (editors need repository push access), change content, save, and verify the new Netlify deploy. This is a Git-backed editor, not an unauthenticated local database. Do not use deprecated Git Gateway for a new setup.

CMS fields: menu categories/groups/items/prices; animation ingredient lists, glass styles and colors; homepage copy; original logo and hero image; gallery; reviews; hours and business contacts; movie-cocktail page entries and sources. Keep copy-field keys unchanged. Cocktail animation names must match menu item names exactly. Changing a title requires updating its animation name too.

## Local preview and rebuild
Run python3 build.py after editing content JSON. Then run python3 -m http.server 8000 from this folder and open http://localhost:8000 . Forms are not delivered on this local server. CMS login/save requires account setup and network access to Decap's CDN. Root-relative links mean double-clicking index.html is NOT the intended preview method.

## Included
Homepage, Cocktails on Film page, contact + consent-based newsletter forms, thank-you page, original logo, venue images, all CMS content and configuration, build script, Netlify settings, and private-inbox instructions. Shop/merchandise features and decorative numbering are excluded. Cocktail animations are click-only and single-active, with reduced-motion support. Movie drinks are editorial, not an assertion of bar availability.

## Deployment status
Locally built and checked, NOT deployed. CMS OAuth login/commit/publish, Netlify form receipt, inbox permissions and notification delivery still require your account setup and a live test. Templates/content contain only public website content; no customer submissions or credentials are included. Validate inherited menu details, reviews and movie sources before launch.
