### Problem: 1948. Delete Duplicate Folders in System

# LeetCode [Hard]
Link: https://leetcode.com/problems/delete-duplicate-folders-in-system

--- 

🧾 Problem Description
You are given a list of folder paths like:

```python
[["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
```
Each path represents a directory in a file system. Some subfolders are exact duplicates, meaning they have the same names and same structure under them.


---
Goal:
Remove all such duplicate folders (and everything inside them), and return the remaining folder structure.

🔍 Example
Input:

```python
paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
```
---
Output:

```python
[["a"],["c"],["a","b"],["c","b"]]
```
Because:
a/b/x/y and w/y are both unique
But full a/b/x/y is a duplicate substructure (under different paths)

----

#### Core Idea
We have to:

Build a Trie (prefix tree) from all paths.

Serialize each subtree using DFS to detect duplicates.

Mark and remove duplicate subtrees.

Traverse what's left and collect valid folder paths.

-------

✅ Steps
Build a tree using nested dicts with a custom TreeNode class.

DFS to serialize every subtree. Store serialization counts in a defaultdict.

On a second DFS, skip serials seen more than once.

Collect remaining paths.