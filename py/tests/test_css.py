# tests - CTCL 2024
# File: /py/tests/test_css.py
# Purpose: Tests for the css.py module
# Created: November 30, 2024
# Modified: November 30, 2024


from serine.css import no_where
def test_no_where():
    example = """
p:where(.class1, .class2, .class3) {
    color: red;
}
div:where(.box, .container) {
    padding: 10px;
}
.other img {
    width: 100%;
}
"""

    expected = """
p.class1, p.class2, p.class3 {
    color: red;
}
div.box, div.container {
    padding: 10px;
}
.other img {
    width: 100%;
}
"""

    result = no_where(example)
    assert result == expected

