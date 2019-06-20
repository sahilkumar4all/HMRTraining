Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set1 = {1,2,3,4,5,6}
>>> set1
{1, 2, 3, 4, 5, 6}
>>> set2 = [1,2,5,6,9,11,12]
>>> set1.union(set2)
{1, 2, 3, 4, 5, 6, 9, 11, 12}
>>> #intersection
>>> set1.intersection(set2)
{1, 2, 5, 6}
>>> 
