import Levenshtein

# Function to load domains into a set
def load_domains(file_path):
    domains_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            domain = line.strip().lower()  # Normalize to lowercase
            domains_set.add(domain)
    return domains_set

# Function to check if a string is not within 3-letter similarity
def is_similar_to_domains(input_string, domains_set):
    input_string = input_string.lower()  # Normalize to lowercase
    for domain in domains_set:
        # Calculate Levenshtein distance between input_string and each domain
        distance = Levenshtein.distance(input_string, domain)
        if distance <= 3 and domain != 0:
            return False  # Input is within 3-letter similarity to a domain
    return True  # Input is not within 3-letter similarity to any domain

# Load the top-10000-domains.txt into a set
domains_set = load_domains('top-10000-domains.txt')

# Example usage
input_string = "amazn.com"
if is_similar_to_domains(input_string, domains_set):
    print(f"'{input_string}' is not within 3-letter similarity to any domain.")
else:
    print(f"'{input_string}' is within 3-letter similarity to a domain.")

# You can change 'input_string' to test other strings.
