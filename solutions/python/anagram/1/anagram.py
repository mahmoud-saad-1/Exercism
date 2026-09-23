def find_anagrams(word, candidates):
    results = []

    for candidate in candidates:
        word_lower = word.lower()
        candidate_lower = candidate.lower()

        if word_lower == candidate_lower:
            continue
    
        if sorted(word_lower) == sorted(candidate_lower):
            results.append(candidate)

    return results
