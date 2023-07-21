### Unveiling Quality in Chatbot Conversations: Quantitative Analysis of Chatbot Requirements

Repository with supplementary material for the paper entitled _Unveiling Quality in Chatbot Conversations: Quantitative Analysis of Chatbot Requirements_.

**Abstract**: As conversational assistants and natural language interfaces proliferate, the demand for a precise understanding of quality software requirements for chatbots becomes increasingly critical. In this work, we adopted a quantitative methodology, scrutinizing a dataset composed of conversational requirements from a diverse range of agile projects for chatbot development, and identified meaningful patterns in the language and structure utilized. Our investigation led to significant findings, revealing the importance of structured documentation, conversation flow, and user interaction in the development of chatbots, with the most desired quality attributes being capability, naturalness, straightforwardness, and clarity. In addition, a significant emphasis was placed on feature development and meeting acceptance criteria. The research also illuminated the iterative nature of chatbot development, with a recurrent presence of verbs related to improvement or refactoring. While less pronounced, the roles of documentation and testing in ensuring chatbot quality and effectiveness were also noted. This work provides valuable insights into chatbot requirements management and the significance of quality attributes in chatbot development.

**Files:**
- _extract_issues.py_: script to mine issues from the repositories;
- _issues_chatbot.csv_: issues retrieved by _extract_issues.py_;
- _filter_issues.py_: script to filter issues with conversational requirements;
- _issues_conversacionais.csv_: issues retrieved by _filter_issues.py_;
- _analyzing-chatbot-issues.ipynb_: notebook with data analysis;
