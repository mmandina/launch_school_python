/*
  EXAMPLE(S)
  3
 / \
1   2
A = 3 and B = 1 returns true
A = 3 and B = 2 returns true
A = 2 and B = 3 returns false

    3
   / \
  1   2
  /   /
 4   5
// A = 3 and B = 5 returns true
// A = 2 and B = 5 returns true
// A = 5 and B = 2 returns false
*/
class TreeNode {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}

// function validAncestor(node, ancestor, descendant) {
//   if (!node) {
//     return false;
//   }

//   const dfs = function (root, path = new Set()) {
//     if (!root) {
//       return false;
//     }
//     if (root.value === descendant && path.has(ancestor)) {
//       return true;
//     }
//     path.add(root.value);
//     return dfs(root.left, path) || dfs(root.right, path);
//   };

//   return dfs(node);
// }

let tree = new TreeNode(2, new TreeNode(3), new TreeNode(4));

const stack = [tree, tree.left];
console.log(stack.find((node) => node.value === 3) ? true : false);
// console.log(stack.find((node)=>node.value === ))
// console.log(validAncestor(root, 3, 1)); //t

// console.log(validAncestor(root, 3, 2)); //t

// console.log(validAncestor(root, 2, 3)); //f

// root = new TreeNode(
//   3,
//   (left = new TreeNode(1, (left = new TreeNode(4)))),
//   (right = new TreeNode(2, (left = new TreeNode(5))))
// );

// console.log(validAncestor(root, 3, 5));

// console.log(validAncestor(root, 2, 5));

// console.log(validAncestor(root, 5, 2));
