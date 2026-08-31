/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        vector<int> ans= {-1,-1};
        ListNode *a=head, *b= head->next, *c=b->next;
        int first=-1, last=-1, mn=INT_MAX , i=1;
        while(c){
            if((b-> val > a->val && b->val > c->val)|| (b->val <a->val && b-> val <c->val)){
                if(first==-1) first =last=i;
                else{
                    mn=min(mn,i-last);
                    last=i;
                }
            }
            i++;
            a=b;
            b=c;
            c=c->next;
        }
        if(first!=last) ans= {mn, last-first};
        return ans;
    }
};