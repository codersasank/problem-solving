#include<stdio.h>
#define MAX 20

int priority(char ch) {

    switch(ch) {

        case '(':
        case ')':
            return 3;
        case '/':
        case '%':
        case '*':
            return 2;
        case '-':
        case '+':
            return 1;
        default:
            return 0;
    }

}

int is_operator(char ch) {

    if (ch=='(' || ch==')' || ch =='/' || ch =='%' || ch =='*' || ch=='-' || ch=='+') return 1;
    else return 0;
}

void push(char ch, int *top, char *stack) {

    if(*top==MAX-1) return;
    else {
        *top += 1;
        stack[*top] = ch;
    }
}

char pop(int *top, char *stack) {

    if(*top==-1) return '\0';
    else {
        *top -= 1;
        return stack[*top+1];
    }
}

void print(int top, char *stack) {

    for(int i=0; i<=top; i++) printf("%c ", stack[i]);
}

char peek(int top, char *stack)
{
    return stack[top];
}

int is_empty(int top) {

    if(top==-1) return 1;
    else return 0;
}


int main() {

    char s[MAX];
    char op_stack[MAX], out_stack[MAX];
    int top_op=-1, top_out=-1;

    printf("Enter an infix expression: ");
    scanf("%s", s);
    printf("After converting to postfix, the expression is : ");

    for(int i=0; s[i]!='\0'; i++) {

        if(!is_operator(s[i])) {
            push(s[i], &top_out, out_stack);
        }
        else {
                if ( s[i]==')' && !is_empty(top_op) ) {
                    while(! (peek(top_op, op_stack)=='(') ) {

                        char ch = pop(&top_op, op_stack);
                        push(ch, &top_out, out_stack);
                    }
                    pop(&top_op, op_stack);
                    continue;
                }

                else if (is_empty(top_op) || (priority(s[i]) >  priority(peek(top_op, op_stack)) ) || peek(top_op, op_stack)=='(' )  {
                        push(s[i], &top_op, op_stack);
                        continue;
                }

                else {
                    char ch = pop(&top_op, op_stack);
                    push(ch, &top_out, out_stack);
                    i--;
                    continue;
                }
        }

    }

    while(!is_empty(top_op)) {
        char ch = pop(&top_op, op_stack);
        push(ch, &top_out, out_stack);
    }

    print(top_out, out_stack);
}
