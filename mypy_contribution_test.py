

from typing import TypeVar, Union
T = TypeVar("T")

def func(default: T) -> Union[str, T]: ...

def test() -> None:
    tag_name: Union[str, int]
    tag_name = func(1.1)
    reveal_type(tag_name)


'''
from typing import TypeVar, Generic
T = TypeVar('T')
S = TypeVar('S')
class Node(Generic[T, S]):
    def __init__(self, x: T, y: S) -> None:
        ...

IntNode = Node[int, S]
IntIntNode = Node[int, int]
SameNode = Node[T, T]

n = Node(1, 1) # type: IntIntNode
n1 = Node(1, 'a') # type: IntIntNode # E: Argument 2 to "Node" has incompatible type "str"; expected "int"

m = Node(1, 1) # type: IntNode
m1 = Node('x', 1) # type: IntNode # E: Argument 1 to "Node" has incompatible type "str"; expected "int"
m2 = Node(1, 1) # type: IntNode[str] # E: Argument 2 to "Node" has incompatible type "int"; expected "str"

s = Node(1, 1) # type: SameNode[int]
reveal_type(s) # N: Revealed type is "__main__.Node[builtins.int, builtins.int]"
s1 = Node(1, 'x') # type: SameNode[int] # E: Argument 2 to "Node" has incompatible type "str"; expected "int"

#'''
