import re
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_similarity(response):
    clean_text = lambda text: re.sub(r'[^\w\s.]', '', text)

    response = response.json()['data']['data']

    result = {'responses': [], 'citations': []}

    # Iterate over each response dictionary
    for value in response:
        # Clean the long text response
        long_text = clean_text(value['response'])

        # Extract the source contexts, IDs, and links
        sources = [{'id': item['id'], 'context': clean_text(item['context'])} for item in value['source']]

        # Fit and transform the long text and source contexts
        vectorizer = CountVectorizer()

        X = vectorizer.fit_transform([long_text] + [source['context'] for source in sources])

        # Calculate cosine similarity between long text and each source context
        similarities = cosine_similarity(X[0], X[1:])

        # Initialize list to store similar sources
        similar_sources = []

        # Iterate over each similarity score and source
        for source, similarity_score in zip(sources, similarities[0]):
            # Check if similarity score is >= 0.50
            if similarity_score >= 0.40:
                # Append ID, context, and similarity score to similar_sources
                similar_sources.append(
                    {'id': source['id'], 'context': source['context'], 'similarity_score': similarity_score})

        # Append response and similar sources to result
        result['responses'].append({'text': long_text})
        result['citations'].append(similar_sources)

    return json.dumps(result)