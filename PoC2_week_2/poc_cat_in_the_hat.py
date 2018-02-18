"""
SOURCE: http://www.codeskulptor.org/#poc_cat_in_the_hat.py
MODIFIED: http://www.codeskulptor.org/#user43_gVXgGkhKRS_0.py
Recursion according to the "Cat in the Hat"
"""
idx = 0


def get_next_cat(current_cat):
    """
    Helper function to get next cat
    """
    if current_cat == "Cat in the Hat":
        return "Little Cat A"
    elif current_cat != "Little Cat Z":
        return "Little Cat " + chr(ord(current_cat[-1]) + 1)
    else:
        return "Voom"


def clean_up(helper_cat, n):
    """
    Recursive function that prints out story
    """
    if helper_cat == "Voom":
        # print helper_cat + ": I got this. Mess is all cleaned up!"
        print 'Function clean_up was called', n + 1, 'times'
    else:
        next_cat = get_next_cat(helper_cat)
        # print helper_cat + ": I'll have", next_cat, "clean up!"
        clean_up(next_cat, n + 1)


if __name__ == '__main__':
    # get those cats to work!!!!!
    clean_up("Cat in the Hat", 0)