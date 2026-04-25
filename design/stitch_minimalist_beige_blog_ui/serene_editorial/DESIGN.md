---
name: Serene Editorial
colors:
  surface: '#fdf8f6'
  surface-dim: '#ddd9d7'
  surface-bright: '#fdf8f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f7f3f1'
  surface-container: '#f1edeb'
  surface-container-high: '#ebe7e5'
  surface-container-highest: '#e5e2e0'
  on-surface: '#1c1b1a'
  on-surface-variant: '#474740'
  inverse-surface: '#31302f'
  inverse-on-surface: '#f4f0ee'
  outline: '#78776f'
  outline-variant: '#c9c7bd'
  surface-tint: '#5f5f54'
  primary: '#33332a'
  on-primary: '#ffffff'
  primary-container: '#4a4a40'
  on-primary-container: '#bbb9ad'
  inverse-primary: '#c8c7ba'
  secondary: '#725a39'
  on-secondary: '#ffffff'
  secondary-container: '#fbdbb0'
  on-secondary-container: '#765f3d'
  tertiary: '#373136'
  on-tertiary: '#ffffff'
  tertiary-container: '#4e474d'
  on-tertiary-container: '#c0b6bd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e3d5'
  primary-fixed-dim: '#c8c7ba'
  on-primary-fixed: '#1c1c14'
  on-primary-fixed-variant: '#47473d'
  secondary-fixed: '#feddb3'
  secondary-fixed-dim: '#e1c299'
  on-secondary-fixed: '#281801'
  on-secondary-fixed-variant: '#584324'
  tertiary-fixed: '#ebdfe7'
  tertiary-fixed-dim: '#cec4cb'
  on-tertiary-fixed: '#1f1a1f'
  on-tertiary-fixed-variant: '#4c454b'
  background: '#fdf8f6'
  on-background: '#1c1b1a'
  surface-variant: '#e5e2e0'
typography:
  h1:
    fontFamily: manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: workSans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: workSans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: workSans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-max: 1120px
  gutter: 1.5rem
  margin-mobile: 1rem
  stack-sm: 0.5rem
  stack-md: 1.5rem
  stack-lg: 3rem
---

## Brand & Style
The brand personality is calm, intellectual, and inviting. It targets readers and writers who value focus and clarity over visual noise. The emotional response is one of warmth and digital wellness—reducing eye strain and cognitive load through a carefully curated minimalist aesthetic. 

The design style is a refined **Minimalism** with subtle **Tonal Layering**. It prioritizes generous whitespace and a restricted, high-quality color palette to ensure the content remains the focal point. This design system avoids aggressive marketing patterns in favor of a sophisticated, editorial atmosphere that feels both modern and timeless.

## Colors
The palette is built on a foundation of warm neutrals. The base background uses a crisp, off-white "linen" (#FAF9F6), while UI surfaces and cards utilize a richer "warm beige" (#F5F5DC) to create soft, organic contrast. 

The primary color is a deep charcoal-olive, used for high-importance text and iconography to maintain readability without the harshness of pure black. The secondary color is a muted tan, reserved for subtle accents, category tags, or hover states that require a gentle emphasis.

## Typography
The typography system uses a pairing of two highly legible sans-serifs. **Manrope** is used for headlines to provide a modern, geometric, and balanced structure that feels professional. **Work Sans** is employed for body copy and labels; its slightly wider apertures and neutral personality ensure long-form reading comfort on both desktop and mobile screens. 

Hierarchy is established through weight and scale rather than color variation. Body text should maintain a generous line height (1.6) to enhance the "airy" feel of the design system.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model for desktop, centered within the viewport, transitioning to a fluid single-column layout for mobile devices. The rhythm is based on an 8px base unit.

Content is organized into a primary reading column with a maximum width of 1120px to prevent excessive line lengths. Vertical rhythm is driven by "stacks"—consistent spacing between headlines, paragraphs, and components—ensuring that the whitespace feels intentional and structured.

## Elevation & Depth
Depth is conveyed through **Ambient Shadows** and **Tonal Layers**. Rather than using heavy drop shadows, this design system employs "soft glow" shadows—extremely diffused, low-opacity (5-8%) blurs with a slight warm tint (#4A4A40) to match the palette.

Surface levels are defined as follows:
- **Level 0 (Base):** #FAF9F6 (The main canvas).
- **Level 1 (Card/Surface):** #F5F5DC (Slightly darker, used for blog post cards and sidebars).
- **Elevated State:** Level 1 surfaces gain a soft ambient shadow on hover to indicate interactivity.

## Shapes
The shape language is defined by a consistent **Rounded** (0.5rem) corner radius. This softens the overall aesthetic, moving away from the clinical feel of sharp edges toward a more approachable, modern look. Large components like featured images or primary containers should use `rounded-xl` (1.5rem) to emphasize the soft, "pill-like" quality of the UI.

## Components
- **Cards:** Blog post cards feature a #F5F5DC background, `rounded-lg` corners, and a very subtle 1px border (#E5E4D2). Images within cards should have a 0.5rem radius.
- **Buttons:** Primary buttons use the deep charcoal-olive background with white text; they are fully rounded (pill-shaped) to distinguish them from cards. Secondary buttons use a simple text-and-underline style or a light tan border.
- **Chips/Tags:** Used for categories. They should be small, capitalized, with a light tan background and `rounded-full` (pill) shape.
- **Input Fields:** Minimalist design with a bottom-border only or a very light #E5E4D2 fill. No heavy strokes. Focus states should be indicated by a shift to the primary color.
- **Lists:** Clean, bullet-less lists for navigation and archives, using generous vertical padding (1rem) between items to maintain the minimalist breathability.
- **Search Bar:** A prominent, rounded input field at the top of the board with a soft ambient shadow to signify its role as a primary tool.