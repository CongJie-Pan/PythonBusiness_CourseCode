from apyori import apriori

# Sample dataset of transactions
data = [
    ['milk', 'bread', 'eggs'],
    ['milk', 'bread'],
    ['bread', 'butter'],
    ['milk', 'eggs'],
    ['bread', 'eggs', 'butter'],
    ['milk', 'bread', 'eggs', 'butter']
]

# Run Apriori algorithm with specific minimum thresholds
association_rules = apriori(data, min_support=0.3, min_confidence=0.6, min_lift=1.2, max_length=2)
association_results = list(association_rules)

# Print out each rule along with support, confidence, and lift
for item in association_results:
    # Extracting pair of items involved in the rule
    pair = item.items
    items = [x for x in pair]

    # If the rule has two items, display the rule details
    if len(items) == 2:
        print(f"Rule: {items[0]} -> {items[1]}")
        print(f"Support: {item.support}")
        print(f"Confidence: {item.ordered_statistics[0].confidence}")
        print(f"Lift: {item.ordered_statistics[0].lift}")
        print("=====================================")

# ============================================

data = [['r', 'z', 'h', 'j', 'p'],
       ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
       ['z'],
       ['r', 'x', 'n', 'o', 's'],
       ['y', 'r', 'x', 'z', 'q', 't', 'p'],
       ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]

association_rules = apriori(data, min_support=0.16, min_confidence=0.2, min_lift=3, max_length=2)
association_results = list(association_rules)
print(association_results)

for item in association_results:
   pair = item[0]
   items = [x for x in pair]
   print("Rule: " + items[0] + " -> " + items[1])
   print("Support: " + str(item[1]))
   print("Confidence: " + str(item[2][0][2]))
   print("Lift: " + str(item[2][0][3]))
   print("=====================================")

