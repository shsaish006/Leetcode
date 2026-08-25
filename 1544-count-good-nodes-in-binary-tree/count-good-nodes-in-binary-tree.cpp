/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
int dfs(TreeNode* r, int mx){
    if(!r) return 0;
    mx=max(mx,r->val);
    return (r->val >=mx)+dfs(r->left,mx)+dfs(r->right,mx);
}
    int goodNodes(TreeNode* root) {
        return dfs(root,-1e9);
        
    }
};