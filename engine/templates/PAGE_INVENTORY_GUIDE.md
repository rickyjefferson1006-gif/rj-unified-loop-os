# Page Inventory Guide

The page inventory is the source of truth for every public, authenticated, administrative, support, content, and legal route. Create `.experience-build/site-map.json` before page implementation.

For every page, record:

- stable ID and final route;
- page type, purpose, audience, search intent, and primary query;
- unique title, description, canonical URL, and indexing directive;
- required headings, factual claims, answer blocks, schema types, and entity IDs;
- internal links expressed as stable page IDs;
- primary call to action and conversion event;
- authentication, role, data, empty, loading, error, success, and permission states;
- desktop, tablet, mobile, accessibility, analytics, and consent requirements;
- author, reviewer, owner, review date, and evidence references.

Do not create thin variants for keyword permutations. Consolidate pages that serve the same user need. A route may be omitted only when the approved requirements say it is unnecessary.

The inventory must include applicable 404, 500, offline, maintenance, search, sitemap, onboarding, account, settings, billing, support, admin, and legal surfaces. Every internal link target must resolve to an inventory ID.
