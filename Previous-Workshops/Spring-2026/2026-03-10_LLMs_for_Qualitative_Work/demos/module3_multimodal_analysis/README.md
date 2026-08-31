# Module 3: Multimodal Analysis of Vaping Content with Gemini

## Overview

This module demonstrates how large language models with vision capabilities (specifically Google Gemini) can assist with qualitative analysis of visual and multimodal content. Using the anchor paper "The Normalization of Vaping on TikTok," we replicate aspects of human visual coding by asking Gemini to observe, describe, and interpret images and video.

**Core Research Question:** How do social media videos normalize vaping as an everyday, acceptable activity through visual framing and messaging?

---

## Anchor Paper

**Citation:**
Jung, S., et al. (2024). "The Normalization of Vaping on TikTok Using Computer Vision, Natural Language Processing, and Qualitative Thematic Analysis: Mixed Methods Study." *Journal of Medical Internet Research*, 26, e55591.

**PMC (open access):** https://pmc.ncbi.nlm.nih.gov/articles/PMC11425021/

**Key Findings:**
- Analyzed 14,002 TikTok posts tagged #vaping or #vape
- Used automated computer vision and NLP to identify patterns at scale
- Conducted qualitative thematic analysis on a stratified sample
- Found that videos predominantly emphasize aesthetics, social situations, and product appeal
- Health warnings and educational messaging are rare; risk communication is minimal
- Visual normalization occurs through integration with lifestyle, peer bonding, and aspirational imagery

**Why It Matters for This Module:**
The JMIR study shows that multimodal content analysis requires both computational scale and human interpretation. LLMs with vision can replicate some aspects of human coding but have systematic limitations. By reproducing their methodology on a smaller scale with Gemini, students will understand:
1. Where LLMs excel at multimodal analysis (concrete observation, visual feature identification)
2. Where they struggle (cultural interpretation, subtle normalization cues, emotional context)
3. How to design prompts and frameworks that maximize LLM utility while accounting for limitations

---

## Files in This Directory

| File | Purpose |
|------|---------|
| **SOURCE.md** | Detailed guide to finding images and video for the demo, copyright considerations, and upload instructions |
| **prompts.txt** | Four sequential Gemini prompts for multimodal analysis (structured observation, public health lens, cross-image comparison, video analysis) |
| **coding_framework.txt** | Visual coding scheme adapted from the JMIR study, with 6 code categories and teaching notes |
| **README.md** | This file—overview, learning objectives, instructions, and discussion questions |
| **images/** | 6 figures from Jung et al. (2024), covering all 5 TikTok themes |
| **video/** (optional) | Short (~2-3 min) publicly available video clip about vaping |

---

## Learning Objectives

By the end of this module, students will be able to:

1. **Understand multimodal LLM capabilities:**
   - What vision models like Gemini can and cannot do
   - How to structure prompts for multimodal analysis
   - When to trust LLM observations vs. when to rely on human expertise

2. **Apply qualitative coding frameworks to visual data:**
   - Use the coding scheme (setting, aesthetics, product visibility, social context, text framing, normalization cues)
   - Identify patterns and themes in visual content
   - Compare manual codes with LLM-generated observations

3. **Recognize normalization strategies in media:**
   - Identify visual and textual techniques that normalize behavior
   - Understand how aesthetics, social context, and framing shape perception
   - Analyze missing messaging (what's *not* shown) as a form of normalization

4. **Evaluate LLM limitations in qualitative research:**
   - Recognize where LLMs miss subtle cultural/emotional cues
   - Understand the importance of human-AI collaboration in content analysis
   - Think critically about using AI to assist with qualitative work

---

## Before the Demo: Preparation (Faculty/TA)

1. **Gather images and/or video** (see SOURCE.md for detailed sourcing instructions)
   - Option A (Recommended): Extract Figures from the JMIR paper (https://www.jmir.org/2024/1/e55591)
   - Option B (Alternative): Search for public health campaign materials, YouTube clips, or educational resources
   - Option C (Advanced): Create synthetic TikTok-style mockups

2. **Prepare Gemini access:**
   - Ensure all students/instructors have access to https://gemini.google.com (free with Google account)
   - No API key required for web interface
   - Test file uploads in advance: images and video should upload without errors

3. **Print or share the coding framework:**
   - Distribute coding_framework.txt to students before the demo
   - Familiarize students with the 6 code categories
   - Optional: Have students manually code one image *before* seeing Gemini's analysis

4. **Review prompts:**
   - Read through prompts.txt and anticipate responses
   - Consider which images are best for which prompts
   - Decide whether to do live demo or pre-recorded Gemini responses (live is better for interactivity)

---

## During the Demo: Step-by-Step Instructions

### SETUP (5 minutes)

1. Open https://gemini.google.com in browser (shared screen or projector)
2. Have images/video ready in a folder or browser tabs
3. Display the coding_framework.txt alongside Gemini for reference
4. Show students the anchor paper (especially title and key findings)

### DEMO FLOW (25 minutes)

**Part 1: Single Image Analysis (10 min)**

1. **Upload first image** to Gemini (click attachment icon, select image)
2. **Run Prompt 1** (Structured Observation):
   - Copy-paste from prompts.txt
   - Ask Gemini to analyze the image
   - Review response on screen with students
3. **Manual coding activity (2 min):**
   - Ask students: "Using the coding framework, what codes would *you* assign to this image?"
   - Ask for 2-3 shout-outs (e.g., "What's the setting? What's the primary normalization strategy?")
   - Compare student codes to Gemini's inferred codes
4. **Key teaching point:**
   - Gemini is excellent at naming concrete visual elements (colors, objects, people)
   - Gemini sometimes misses the cultural interpretation or normalization effect
   - Example: Gemini might say "The image shows a person holding a vape device with clouds" but may not recognize that the aesthetic framing normalizes the activity

**Part 2: Public Health Lens (5 min)**

5. **Run Prompt 2** (Re-coding with Public Health Lens):
   - Copy-paste from prompts.txt
   - Ask Gemini to analyze the SAME image from a public health perspective
   - Compare this response to Prompt 1's response
6. **Key teaching point:**
   - When explicitly prompted to focus on health/risk, Gemini can identify absences (what's NOT shown)
   - This demonstrates that prompt design shapes LLM output
   - But Gemini still won't catch all subtle cultural normalization that a trained human coder would

**Part 3: Cross-Image Comparison (5 min)**

7. **Upload 2-3 more images** (if time permits)
8. **Run Prompt 3** (Cross-Image Comparison):
   - Ask Gemini to identify patterns across the images
   - What shared strategies do they use to normalize vaping?
   - Where do they differ?
9. **Compare patterns to coding framework:**
   - Do images share the same setting codes? Aesthetics? Normalization strategies?
   - Can Gemini identify the larger narrative across multiple pieces of content?

**Part 4: Video Analysis (optional, if time permits)**

10. **Upload video clip** (if using)
11. **Run Prompt 4** (Video Analysis):
    - Ask for timestamped observations
    - Compare video framing to still images
12. **Key teaching point:**
    - Motion, audio, and editing can amplify or diminish normalization effects
    - Video analysis is more complex; Gemini may struggle with subtle audio cues

---

## After the Demo: Discussion & Reflection (15 minutes)

### Discussion Questions for Students

**On LLM Capabilities:**
1. Where did Gemini's analysis match your manual coding? Where did it differ?
2. What types of observations is Gemini best at? (Likely: identifying objects, colors, spatial relationships)
3. What did Gemini miss or misinterpret? (Likely: cultural context, emotional subtext, normalization strategies)
4. How confident would you be using Gemini alone to code hundreds of images for research?

**On Normalization Strategies:**
5. What's the most powerful technique these images use to normalize vaping? (Aesthetic appeal? Social bonding? Integration into lifestyle?)
6. What messages *aren't* present in these images? (Health warnings, age restrictions, risk information)
7. If you were designing a counter-narrative or health intervention, what would you emphasize or change?

**On Human-AI Collaboration:**
8. How could you use Gemini to *assist* human coders rather than replace them?
   - Example: Use Gemini to generate initial descriptive codes, then human coders verify/refine
   - Example: Use Gemini to flag images that *might* contain certain features, then human coders validate
9. What safeguards or validation checks would you put in place if using LLMs for qualitative analysis in a real study?
10. How would you document the role of AI in your methods section?

**On Research Ethics:**
11. We used published figures and/or public health materials for this demo rather than downloading TikTok content directly. Why does that matter?
12. If you were conducting a real analysis of social media content, what ethical considerations would you face?
    - Informed consent? Privacy? Platform policies? Copyright?

---

## Explore Further

### Vision-Capable LLMs to Compare

1. **GPT-4o Vision** (OpenAI)
   - More advanced visual reasoning than Gemini
   - Paid API (but free tier available with limited credits)
   - Better at cultural interpretation (sometimes)

2. **Claude 3.5 Sonnet with Vision** (Anthropic)
   - Multimodal capability; strong at reasoning
   - API access (similar pricing to OpenAI)
   - Excellent at explicit reasoning about limitations

3. **Llama 2 Vision** (Meta)
   - Open-source alternative
   - Can be run locally
   - Limited to image input (no video); slightly less capable than GPT-4o/Claude

**Comparative Activity (if extended):**
- Upload the same image to Gemini, GPT-4o, and Claude
- Run the same prompt on each
- Compare responses: Where do they agree? Differ? Which seems most accurate?
- Discuss: What accounts for differences? Does model choice matter for qualitative coding?

### Related Research & Readings

- **Anchor paper:** Jung et al. (2024). JMIR. https://pmc.ncbi.nlm.nih.gov/articles/PMC11425021/
- **Vaping & social media:** Search PubMed for "e-cigarette social media" or "vaping TikTok" for additional studies
- **Multimodal AI:** Radford et al. (2021). "Learning Transferable Visual Models from Natural Language Supervision." *Proceedings of ICML*.
- **Qualitative coding & AI:** Leavy et al. (2022). "Automated Content Analysis Raises Questions About Editorial Judgment." *Nature Human Behaviour*.

---

## Teaching Notes & Tips

### What Works Well

- **Live demos are better than pre-recorded:** Students engage more when they see real-time responses and can ask questions about unexpected outputs
- **Manual coding first, then Gemini:** If time permits, have students code an image *before* revealing Gemini's analysis. The comparison is more powerful.
- **Use images with clear normalization strategies:** Aesthetic, social, or lifestyle framing are easier for Gemini to identify than subtle symbolic cues.
- **Emphasize the limits:** Students should leave understanding that Gemini is a *tool for assistance*, not replacement for human analysis.

### Common LLM Mistakes to Watch For

- **Over-generalization:** Gemini might say "This image normalizes vaping" when it only describes one feature contributing to normalization
- **Confidence without nuance:** LLMs often sound authoritative even when uncertain; prompt for caveats ("What might I be missing?")
- **Missing negation:** Gemini may not adequately emphasize what's *absent* (health warnings, age restrictions)
- **Emotional projection:** LLMs sometimes infer emotional tone based on limited cues; ask for evidence

### Accessibility & Inclusion

- Provide alt-text descriptions for any images used (especially if discussed without displaying)
- Offer coding_framework.txt in multiple formats (PDF, Google Doc, text) for students using screen readers
- Allow students to use Claude, GPT-4o, or other LLMs if they prefer; framework works with any vision model

### Timing Adjustments

- **Full 50-minute session:** Include all 4 prompts, discussion, and "Explore Further" activities
- **Shortened to 30 minutes:** Focus on Prompts 1-2 (single image + public health lens) and brief discussion
- **Extended to 75+ minutes:** Add comparative analysis (Gemini vs. GPT-4o), manual coding activity, and deeper ethics discussion

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Images won't upload to Gemini | Check file format (PNG, JPG, GIF, WebP) and size (<20 MB). Try different browser if issue persists. |
| Video won't upload | Confirm format (MP4, MOV, AVI, WebM, etc.). Video should be <2 GB and ideally <10 min. Try uploading via API if web interface fails. |
| Gemini response seems off-topic or incoherent | Sometimes happens with very long or complex prompts. Simplify language, break into multiple questions, or re-upload image. |
| Students can't access Gemini | Free access requires Google account. Provide info on how to set up free account if needed. |
| Discussion lags / no student input | Try smaller groups (pair students for pre-demo coding activity), offer multiple response modes (chat, raise hand, anonymous poll). |

---

## Files Checklist

Before running the demo, ensure you have:

- [ ] SOURCE.md (sourcing guide) — complete
- [x] 6 images gathered and saved in images/ (fig4 through fig9)
- [ ] prompts.txt (Gemini prompts) — ready to copy-paste
- [ ] coding_framework.txt — printed or shared with students
- [ ] README.md (this file) — shared with students for context
- [ ] Optional: 1-2 video clip(s) if doing full demo
- [ ] Optional: Printed coding framework or digital version for students to reference during demo
- [ ] Gemini account set up and tested with image/video uploads
- [ ] Backup slides or handouts with key teaching points (in case tech fails)

---

## Questions?

This module is part of the D-Lab "LLMs for Qualitative Work" workshop series. For questions about content, contact the workshop facilitator or consult the anchor paper (Jung et al., 2024).

---

## License & Attribution

These materials are adapted from the research methodology in:

Jung, S., et al. (2024). "The Normalization of Vaping on TikTok Using Computer Vision, Natural Language Processing, and Qualitative Thematic Analysis: Mixed Methods Study." *Journal of Medical Internet Research*, 26, e55591.

The prompts, coding framework, and teaching materials were developed for the D-Lab workshop series and are provided for educational use.
