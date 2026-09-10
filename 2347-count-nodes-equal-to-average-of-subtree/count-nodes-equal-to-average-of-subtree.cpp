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
int ans=0;
pair<int,int> dfs(TreeNode* root){
    if(!root) return {0,0};
    pair<int,int> a=dfs(root->left);
    pair<int,int> b=dfs(root->right);
    int s=a.first+b.first+root->val;
    int n=a.second+b.second+1;
    if(s/n==root->val) ans++;
    return {s,n};
}
    int averageOfSubtree(TreeNode* root) {
        ans=0;
        dfs(root);
        return ans;
        
    }
};