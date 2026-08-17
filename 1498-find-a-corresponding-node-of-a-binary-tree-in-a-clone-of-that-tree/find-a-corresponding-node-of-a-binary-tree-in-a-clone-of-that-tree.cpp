/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* o, TreeNode* c, TreeNode* t) {
        if(!c) return 0;
        if(c->val ==t->val) return c;
        TreeNode* x=getTargetCopy(o,c->left,t);
        return x?x:getTargetCopy(o,c->right,t);
        
    }
};