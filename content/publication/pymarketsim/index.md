---
title: 'A Financial Market Simulation Environment for Trading Agents Using Deep Reinforcement Learning'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Anri Gu
  - Yongzhao Wang
  - Mithun Chakraborty
  - Michael Wellman

# # Author notes (optional)
# author_notes:
#   - 'Equal contribution'
#   - 'Equal contribution'

date: '2024-11-14T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *5th ACM International Conference on AI in Finance*
publication_short: In *ICAIF*

abstract: We present PyMarketSim, a financial market simulation environment designed for training and evaluating trading agents using deep reinforcement learning (dRL). Our agent-based environment incorporates key elements such as private valuations, asymmetric information, and a flexible limit order book mechanism. We demonstrate the efficiency and versatility of our platform through experiments including both single-agent and multi-agent dRL settings. For single-agent settings, we showcase how our environment can be used to learn background trading strategies implemented as recurrent neural networks. These trained response order networks (TRON agents) can flexibly condition their behavior on observed market characteristics. At the multi-agent level, we use empirical game-theoretic techniques to identify equilibrium configurations of TRON agents. Our open-source implementation provides researchers and practitioners with a powerful tool for studying complex market dynamics, developing advanced trading algorithms, and exploring the emergent behaviors of financial ecosystems driven by machine learning.


# Summary. An optional shortened abstract.
summary: An open-source financial market simulation environment designed for training and evaluating trading agents using deep reinforcement learning, facilitating research in complex market dynamics.

tags:
  - Finance
  - Reinforcement Learning
  - Trading Agents
  - Market Simulation

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://dl.acm.org/doi/pdf/10.1145/3677052.3698639'
url_code: 'https://github.com/dipplestix/pymarketsim/tree/master'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
  - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the _Slides_ button to check out the example.
{{% /callout %}}

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/).
