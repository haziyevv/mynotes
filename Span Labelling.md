1. Span labelling is not the same thing as entity extraction
2. Entities have clear token boundaries and are comprised of syntactic units like proper nouns. However, spans often costist of noun phrases and sentence fragments. Also spans can even overlap
3. Spancat has two parts: **suggester** and **classifier**
4. **Suggester** is a custom function that extracts possible span candidates from the text and feeds them to the classifier. Suggester, can be rule-based, can depend on annotations from other components or use machine learning
5. 