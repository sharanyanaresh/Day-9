# Tuple Question

t = ([1,2],[3,4])

Yes, `t[0][0] = 99` works.

Tuples are immutable, meaning the tuple itself cannot change.
However, the objects inside the tuple can be mutable.

Lists are mutable, so we can modify their elements even if they are inside a tuple.


# Duplicate Detection

```python
def find_duplicates(lst):

    seen=set()
    dup=set()

    for x in lst:
        if x in seen:
            dup.add(x)
        else:
            seen.add(x)

    return dup

def unique_to_each(a,b):

    return list((set(a)-set(b)) | (set(b)-set(a)))


---

# STEP 5 — `ai_jaccard.md`

Paste:

```markdown
Prompt used:

"Write a Python function that calculates the Jaccard similarity between two sets of strings. Explain what Jaccard similarity is and where it is used in industry."

AI Code:

```python
def jaccard_similarity(a,b):

    intersection=len(a&b)
    union=len(a|b)

    if union==0:
        return 0

    return intersection/union

set_a={'python','java','sql'}
set_b={'python','sql','docker','aws'}

print(jaccard_similarity(set_a,set_b))


---

# STEP 6 — Run One File

