Joe Jimenez, Ryan Dielhenn, Bohdan Hrotovytskyy, Ryan Goshorn, Matthew Gutierrez  

Professor Beltran  

CS5660  

5 November 2025

\begin{center}
\textbf{\Large Project 1 – Problem Definition}
\end{center}

## What is arXiv?

"arXiv is a curated research-sharing platform open to anyone. As a pioneer in digital open access, arXiv.org now hosts more than two million scholarly articles in eight subject areas, curated by our strong community of volunteer moderators" (arXiv.org, n.d.).

---

## Step 1: What is the Problem?

**Informal Description:**  
It’s hard for researchers to see what kinds of topics exist within a large research field on arXiv without already knowing what to look for. We want to automatically uncover and organize hidden topic patterns across papers.

**Formal Definition:**  
This is an **unsupervised learning problem**, since it involves identifying patterns and structure in unlabeled text data (research paper abstracts or titles).  

- **Input Data (X):** A set of paper abstracts or titles from a chosen arXiv subfield.  
- **Objective:** To find clusters or latent topics that group similar research together, minimizing within-topic differences and maximizing differences between topics.  
- **Approach:** We aim to use topic modeling methods such as Latent Dirichlet Allocation (LDA), Non-negative Matrix Factorization (NMF), or modern transformer-based topic models (e.g., BERTopic) to extract and label coherent topics from unstructured text.  
- **Output:** A structured map of research topics with representative keywords, paper groupings, and temporal trends.

**Problem Summary:**  
While arXiv provides search functionality, users must already know specific keywords or topics they're interested in. This project aims to automatically discover and organize the latent topic structure within a specific arXiv subfield (such as cs.AI, stat.ML, or q-bio), revealing research themes, emerging areas, and connections that aren't explicitly labeled.

**Assumptions:**  
1. The text content of paper abstracts is representative of the research topic.  
2. The chosen arXiv subfield contains enough papers to identify meaningful topic clusters.  
3. Text preprocessing (tokenization, stopword removal, stemming, lemmatization, etc.) can sufficiently clean the data for modeling.  
4. Topic modeling algorithms (e.g., LDA or BERTopic) can capture meaningful themes without supervision.  
5. The number of discovered topics can be tuned to balance interpretability and granularity.  
6. Paper abstracts are written in English or can be standardized for consistent processing.  
7. Metadata fields such as submission date and authors can help analyze topic trends over time.  
8. Computational resources (e.g., GPUs or cloud-based notebooks) will be sufficient for dataset size.  
9. New papers will generally align with previously identified topics, allowing incremental updates.  
10. The dataset is large but not so unbalanced that some topics dominate others.

**Similar Problems:**  
- Clustering **news articles** by topic (e.g., politics, sports, technology) using LDA to find underlying themes.  
- Grouping **scientific abstracts** from PubMed into biomedical topics to identify emerging research in medicine.  
- Organizing **social media posts** (like Reddit or Twitter) into conversational themes or discussion clusters.  
- Categorizing **research conference submissions** automatically by topic to aid reviewers and conference chairs.

**Additional Context:**  
This project’s unsupervised nature makes it suitable for discovery rather than classification. We are not predicting predefined labels but revealing the hidden thematic structure of a research domain. The outcome could serve as the foundation for tools that visualize or recommend research papers based on topic similarity.

---

## Step 2: Why Does the Problem Need to be Solved?

### Motivation
The rapid growth of scientific literature makes it increasingly difficult for researchers to keep up with developments in their field. ArXiv alone adds thousands of new papers monthly, and while broad category labels exist (e.g., cs.AI), these encompass diverse research areas that aren't further organized. Researchers, especially those new to a field or exploring adjacent areas, face the challenge of navigating this vast collection without a clear map of the underlying research landscape. This project addresses the need for automated discovery and organization of research themes, making scientific literature more accessible and discoverable.

**Extended Motivation:**  
For example, a new graduate student entering *machine learning theory (cs.LG)* might be overwhelmed by the variety of subtopics, such as optimization, neural network generalization, or Bayesian inference which are all under the same category. By uncovering latent themes, the student could see which areas are heavily researched, which are emerging, and how they relate. Similarly, a research advisor could use such a system to monitor trends or identify gaps in their group’s focus.

### Solution Benefits
Solving this problem will provide several key benefits:

- **Enhanced discoverability:** Researchers can explore what topics exist within a subfield without prior knowledge of specific keywords.  
- **Trend identification:** Reveals emerging research areas and how topics evolve over time.  
- **Literature review assistance:** Helps researchers conducting literature reviews by organizing papers into coherent themes.  
- **Knowledge gap identification:** Highlights under-explored areas within a subfield.  
- **Cross-topic connections:** Uncovers relationships between different research themes that may not be obvious from category labels alone.  
- **Automated summaries:** Potentially generates summaries of each topic cluster for faster understanding.  
- **Support for recommendation systems:** Enables personalized paper recommendations based on thematic similarity rather than exact keyword matches.

### Solution Use
We envision this solution being used primarily as an exploratory tool for researchers, students, and academics who want to:

- Understand the research landscape of a new subfield they're entering.  
- Identify relevant papers organized by discovered topics rather than just keywords.  
- Track how research themes emerge and evolve over time.  
- Find papers related to broad concepts rather than specific technical terms.  
- Visualize how certain research topics (e.g., “large language models”) grow in popularity over time.  

**Lifetime and Maintenance:**  
As a course project, this will serve as a proof-of-concept demonstration. However, the methodology could be extended into a more robust tool with periodic re-training as new papers are published (e.g., quarterly updates). The main maintenance needs would include updating the dataset, retraining topic models to capture new trends, and potentially refining the number of topics as the field evolves.  
If expanded, the tool could include a web dashboard (e.g., built with Plotly or Streamlit) to visualize topics dynamically and allow user interaction.

---

## Step 3: How Would I Solve the Problem?

### Manual Approach (without ML)
1. **Collect Data:** Manually download paper abstracts and metadata (titles, authors, publication dates) from arXiv’s API for a chosen subfield (e.g., cs.AI).  
2. **Preprocess Text:** Remove stopwords, convert to lowercase, and standardize technical terms.  
3. **Categorize Manually:** Read through each abstract and assign it to a manually created set of topics such as “reinforcement learning,” “transformers,” or “robotics.”  
4. **Track Topic Frequency:** Count how many papers fall into each theme.  
5. **Visualize Results:** Use simple bar charts or word clouds to show the most common research themes.  
6. **Trend Tracking:** Manually compare topics by year to identify growth or decline trends.  
7. **Validation:** Compare your manual grouping to author keywords or titles to check consistency.

### Manual Data Example
- **Subfield:** cs.AI (Artificial Intelligence)  
- **Collected Papers:** 2,000 abstracts from 2024–2025.  
- **Example Manual Topics:** “Reinforcement Learning,” “LLMs and Transformers,” “Explainable AI,” “Ethics in AI,” “Symbolic AI,” “Neuro-Symbolic Integration.”  
- **Observation:** Topics like “Transformers” and “LLMs” dominate, while older themes such as “expert systems” appear less frequently.

### Reflection
Defining this problem helped clarify the difference between *search* and *discovery*, search requires known terms, while topic modeling allows exploration of unknown structures. The challenge was articulating the unsupervised nature of the problem clearly, since there are no labels to train on. This process reinforced the importance of understanding both the data source and user need before choosing an AI method.

**Additional Reflection:**  
While exploring this problem, we realized that defining what constitutes a “topic” is itself subjective. The difficulty lies not in collecting data, but in ensuring that discovered clusters are interpretable and meaningful to researchers. Balancing algorithmic accuracy with human readability will be a central challenge. This exercise also highlighted how AI can amplify knowledge discovery by automating what used to be purely manual literature synthesis.

---

## Data Source
We will use the **arXiv metadata dataset**, available on Kaggle or via the **arXiv API**, focusing on a specific category to keep the project scope manageable. The dataset contains fields such as paper titles, abstracts, authors, categories, and submission dates.  

Example resource:  
- [arXiv Metadata Dataset on Kaggle](https://www.kaggle.com/datasets/Cornell-University/arxiv)  
- [arXiv API Documentation](https://arxiv.org/help/api)  

The team will collectively decide which subfield to analyze (e.g., cs.AI, stat.ML, or q-bio) based on interest and computational feasibility.

**Potential Data Size:** 50,000–100,000 papers per subfield.  
**Data Preparation Steps:** Cleaning abstracts, removing duplicates, tokenization, and converting text to vector form (TF-IDF or embeddings).

---

## Citation
arXiv.org. (n.d.). *About arXiv*. Retrieved November 5, 2025, from https://arxiv.org/about
