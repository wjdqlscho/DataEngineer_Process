from collections import Counter
import math

# Step 1: Sample documents
# Each document is a string, representing some text content.
documents = [
    "text mining algorithms analyze text",
    "text data mining finds patterns in text",
    "patterns and algorithms are used in text mining"
]

# Step 2: Preprocess documents and calculate term frequencies (TF)
# For each document, split it into words and count occurrences using Counter.
tf = [Counter(doc.split()) for doc in documents]

# Step 3: Calculate document frequency (DF) for each term
# DF counts the number of documents containing each term.
df = Counter()
for doc_tf in tf:
    df.update(doc_tf.keys())

# Step 4: Calculate TF-IDF for each term in each document
# use the formula TF-IDF = TF * log(N/DF), where N is the total number of documents.
N = len(documents)
tf_idf = []
for doc_index, doc_tf in enumerate(tf):
    doc_tfidf = {}
    for term, count in doc_tf.items():
        idf = math.log(N/df[term])  # Inverse Document Frequency (IDF)
        doc_tfidf[term] = count * idf
    tf_idf.append(doc_tfidf)

# Step 5: Display TF-IDF scores
# Print TF-IDF scores for each documents.
for doc_index, scores in enumerate(tf_idf):
    print(f"Document {doc_index + 1}")
    for term, score in scores.items():
        print(f" {term}: {score:.2f}")