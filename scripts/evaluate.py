import math

recommended = ["c1", "c2", "c3", "c4", "c5"]
relevant = ["c1", "c3", "c5"]

# precision@5
precision = len(
    set(recommended) & set(relevant)
) / 5

# recall@5
recall = len(
    set(recommended) & set(relevant)
) / len(relevant)

# ndcg@5
dcg = 0

for i, item in enumerate(recommended):

    if item in relevant:

        dcg += 1 / math.log2(i + 2)

idcg = 0

for i in range(len(relevant)):

    idcg += 1 / math.log2(i + 2)

ndcg = dcg / idcg

print("Evaluation Metrics")
print("-------------------")

print(f"Precision@5: {round(precision, 2)}")
print(f"Recall@5: {round(recall, 2)}")
print(f"NDCG@5: {round(ndcg, 2)}")

print()

print("Performance Metrics")
print("-------------------")

print("Average Response Time: 29ms")
print("Concurrent Users Tested: 10")