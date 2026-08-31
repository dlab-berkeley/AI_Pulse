# Source Materials for Module 3: Multimodal Analysis of Vaping Content

## Anchor Paper

**Citation:**
Jung, S., et al. (2024). "The Normalization of Vaping on TikTok Using Computer Vision, Natural Language Processing, and Qualitative Thematic Analysis: Mixed Methods Study." *Journal of Medical Internet Research*, 26, e55591.

**PMC (open access, with all figures):** https://pmc.ncbi.nlm.nih.gov/articles/PMC11425021/
**JMIR:** https://www.jmir.org/2024/1/e55591
**DOI:** 10.2196/55591

**Key Details:**
- Dataset: 14,002 TikTok posts with #vaping or #vape hashtags
- Methods: Automated visual coding (computer vision), NLP-based text analysis, and manual qualitative coding
- Research focus: How visual framing and language normalize vaping as an everyday, lifestyle activity among young adults
- Key finding: Videos emphasize aesthetics, social situations, and product appeal rather than health risks; rarely include educational or cautionary messaging

**Why it matters for this module:**
The JMIR paper demonstrates that LLMs with vision capabilities (like Gemini) can replicate aspects of human coding at scale. We'll use this framework to conduct similar multimodal analysis on a smaller set of images to understand *how* LLMs observe visual content and *where* they differ from trained human coders.

---

## Images for Demo (Sourcing Instructions)

### Constraints & Alternatives

**Why we can't use TikTok screenshots directly:**
- TikTok's Terms of Service restrict downloading and redistributing video content
- Copyright and user privacy concerns with unmodified screenshots
- Platform's evolving policies on third-party tool usage

### Option A: Use Figures from the PMC Paper (Recommended)

The paper has 9 figures. The best ones for the demo are Figures 4-9, which show actual TikTok screenshots organized by theme. Right-click each link below and "Save Image As":

**Figure 4 -- Theme Overview (USE THIS FIRST)**
All 5 themes side-by-side with representative screenshots. Perfect for cross-image comparison (Prompt 3).
https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2370/11425021/5aa235fd84c8/jmir_v26i1e55591_fig4.jpg
Save as: `fig4_theme_overview.jpg`

**Figure 5 -- Theme 1: General Vape (3 subclusters)**
(A) Active vaping, (B) Choosing not to vape, (C) Health-related. Good for Prompt 1 (structured observation).
https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2370/11425021/32b69c2cc5e8/jmir_v26i1e55591_fig5.jpg
Save as: `fig5_general_vape.jpg`

**Figure 7 -- Theme 3: Vape Product Marketing (2 subclusters)**
(A) Showcasing devices, (B) Product displays with marketing text. Good for Prompt 2 (public health lens).
https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2370/11425021/0ef3baa3528d/jmir_v26i1e55591_fig7.jpg
Save as: `fig7_product_marketing.jpg`

**Figure 6 -- Theme 2: Vaping Cessation (2 subclusters)**
(A) Quitting attempts, (B) Health awareness. Useful for contrasting pro- and anti-vaping framing.
https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2370/11425021/jmir_v26i1e55591_fig6.jpg
Save as: `fig6_vaping_cessation.jpg`

**Figure 8 -- Theme 4: TikTok Influencers (2 subclusters)**
Influencer-driven vaping content. Good for discussing normalization through social media personalities.
https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2370/11425021/jmir_v26i1e55591_fig8.jpg
Save as: `fig8_tiktok_influencers.jpg`

**Figure 9 -- Theme 5: Vape Brands (2 subclusters)**
Brand-focused content. Good contrast for normalization analysis.
https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2370/11425021/93e63a333123/jmir_v26i1e55591_fig9.jpg
Save as: `fig9_vape_brands.jpg`

These are published, open-access academic figures from PubMed Central; educational use is appropriate.

**Note:** Figures 5-9 contain images with blurred faces from the original paper. No additional anonymization is needed.

### Option B: Public Health Campaign Images (Contrast Material)

If Figures 1-3 are unavailable, search for publicly available educational content:

**Suggested search strategies:**

1. **Lifestyle/Aesthetic Vaping Post:**
   - Search: "vaping aesthetic photography free image" or "vape cloud stock photo"
   - Sources: Unsplash, Pexels, Pixabay (search filters for "vaping" or "smoke")
   - Look for high-saturated colors, cool lighting, artistic framing

2. **Product Review/Unboxing Post:**
   - Search: "vape unboxing YouTube screenshot" or "vape product review"
   - Sources: YouTube thumbnails from public health or news review videos (screenshot allowed for educational use)
   - Look for product-centered framing, text overlays, comparison shots

3. **Vape Trick Video Still:**
   - Search: "vape trick tutorial YouTube" or "cloud competition video"
   - Sources: Public YouTube videos (screenshot the frame where trick is highlighted)
   - Look for technical focus, performance context, skill demonstration

4. **Everyday Activity Integration:**
   - Search: "studying with vape" or "social vaping photo"
   - Sources: News articles discussing vaping culture, public health infographics
   - Look for casual integration into normal activities (eating, studying, socializing)

**Sources for finding these images:**
- **JMIR open-access papers:** Search PubMed for vaping + social media studies (many include figures)
- **YouTube:** Educational channels about vaping culture or public health (screenshot for analysis)
- **News outlets:** CNN, BBC, NPR, STAT News often publish articles on vaping trends with images
- **Stock photo sites:** Unsplash, Pexels, Pixabay (filter by "vaping," "smoke," "social media")
- **NIH/CDC resources:** CDC.gov and NIH image galleries have public health campaign materials

### Option C: Create Synthetic Examples (Advanced)

If obtaining images is difficult:
1. Use a design tool (Canva, Adobe Express) to create mockups of TikTok-style layouts
2. Include realistic elements: phone UI, usernames, engagement metrics, visual filters
3. Label clearly as "synthetic examples for educational demo"

---

## Video for Demo

**Suggested sources for a short video clip (~2-3 minutes):**

### Option A: YouTube Public Health Documentary (Recommended)

- Search: "vaping culture documentary" or "teen vaping news segment"
- Examples:
  - PBS NewsHour segments on youth vaping (publicly available on YouTube)
  - American Lung Association educational videos
  - Local news health segments on vaping trends
- **How to use:**
  - Download using a free tool (e.g., youtube-dl or yt-dlp) if local policy allows
  - Alternatively: Play the video in a browser and describe the timestamped observations for the demo
  - Ensure fair use: use brief excerpt (under 10% of original), for educational/commentary purposes

### Option B: TED Talks or Educational Series

- Search for: "TED talks vaping" or "Coursera vaping public health"
- Many such videos explicitly permit educational use
- Screenshot or clip the most relevant 2-3 minute segment

### Option C: Screencast Your Own Observation

- Watch a publicly available vaping-related YouTube video
- Use screen recording software (OBS Studio, free) to capture a 2-3 minute clip
- Narrate your observations in real-time for the demo
- This avoids re-distribution concerns while demonstrating the analysis method

---

## File Organization

Once you've gathered images and/or a video, organize them as:

```
module3_multimodal_analysis/
├── SOURCE.md                    (this file)
├── README.md                    (overview & instructions)
├── prompts.txt                  (exact Gemini prompts)
├── coding_framework.txt         (visual coding scheme)
├── images/
│   ├── image1_aesthetic.png
│   ├── image2_unboxing.png
│   ├── image3_tricks.png
│   └── image4_everyday.png
└── video/ (optional)
    └── vaping_video_clip.mp4 (or .webm)
```

---

## Uploading to Gemini

### Step 1: Prepare Images

- **Supported formats:** PNG, JPG, JPEG, GIF, WebP
- **File size:** Under 20 MB per image
- **Resolution:** 1000+ pixels on longest edge for best results
- **Orientation:** Portrait or landscape are both fine; use original orientation

### Step 2: Prepare Video

- **Supported formats:** MP4, MPEG, MOV, AVI, FLV, MKV, WebM, WMV, 3GPP
- **File size:** Under 2 GB
- **Duration:** Up to 1 hour (our 2-3 min clip is well within limits)
- **Codec:** H.264 (most common)

### Step 3: Upload to Gemini

**Via Gemini Web Interface:**
1. Open https://gemini.google.com
2. Click the attachment icon (paperclip or image icon) in the message box
3. Select "Upload" → choose your image(s) or video file
4. Paste your prompt (from `prompts.txt`) after upload completes
5. Submit the prompt

**Via API (if using Gemini API programmatically):**
- See: https://ai.google.dev/tutorials/upload_files
- Requires API key; upload files, get file URIs, include in prompt

---

## Additional Resources

- **JMIR Paper full text (PMC open access):** https://pmc.ncbi.nlm.nih.gov/articles/PMC11425021/
- **Gemini Upload Documentation:** https://support.google.com/gemini/answer/13674243
- **Vaping & Social Media Research:** Search PubMed for "vaping social media" or "e-cigarette TikTok"
- **Public Health Data:** CDC.gov has freely available youth vaping statistics and educational materials

---

## Teaching Notes

- **Emphasize:** Multimodal models like Gemini are excellent at *describing visible objects and spatial relationships* but may struggle with *cultural interpretation* and *emotional subtext*
- **Compare:** Ask students to code the same image manually, then compare their codes with Gemini's output—where do they agree? Differ?
- **Limitations:** LLMs may miss subtle normalization cues that human coders trained on vaping literature would catch
- **Ethics:** Discuss informed consent and representation when analyzing real social media content; using published paper figures or synthesized examples sidesteps these concerns
