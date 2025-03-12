---
title: 'Market Making with Learned Beta Policies'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Yongzhao Wang
  - Rahul Savani
  - Anri Gu
  - admin
  - Theodore Turocy
  - Michael P Wellman

date: '2024-11-14T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2024-07-01T00:00:00Z'
# Set to true to hide this page from being published
draft: true

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the 5th ACM International Conference on AI in Finance*
publication_short: In *ICAIF*

abstract: 'In market making, a market maker (MM) can concurrently place many buy and sell limit orders at various prices and volumes, resulting in a vast action space. To handle this large action space, beta policies were introduced, utilizing a scaled beta distribution to concisely represent the volume distribution of an MM's orders across different price levels. However, in these policies, the parameters of the scaled beta distributions are either fixed or adjusted only according to predefined rules based on the MM's inventory. As we show, this approach potentially limits the effectiveness of market-making policies and overlooks the significance of other market characteristics in a dynamic market. To address this limitation, we introduce a general adaptive MM based on beta policies by employing deep reinforcement learning (RL) to dynamically control the scaled beta distribution parameters and generate orders based on current market conditions.'

# Summary. An optional shortened abstract.
summary: 'Using deep reinforcement learning to dynamically control beta distribution parameters for market making policies.'

tags:
  - Finance
  - Market Making
  - Reinforcement Learning

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://dl.acm.org/doi/pdf/10.1145/3677052.3698623'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

{{% callout note %}}
Click the _Cite_ button above to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

This paper addresses the challenge of efficiently managing a large action space in market making by using learned beta policies. Market makers traditionally place multiple buy and sell limit orders at various prices, creating a vast decision space. Our approach uses deep reinforcement learning to dynamically adjust beta distribution parameters that control order placement based on current market conditions, improving upon previous methods that used fixed parameters or simple inventory-based adjustments. 