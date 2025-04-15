# USL Hosted Multi-Language App for Render

This app lets users:
- Upload `.usl` files
- Transpile to selected languages (1 or all)
- Download full output as `.zip`
- Includes "USL" option to preserve original

## 🚀 How to Deploy on Render

1. Go to [https://render.com](https://render.com)
2. Click "New Web Service" and connect your GitHub (optional)
3. Upload this zip or sync your repo
4. Set the following:
   - Environment: Python 3.x
   - Start Command: `python app.py`
   - Build Command: *(leave blank)*

## 🔁 To Monetize:
- Attach Gumroad or Stripe payment buttons (paid unlock for `.zip`)
- Add user auth for API access tiers
- Use Paywall before sending ZIP

