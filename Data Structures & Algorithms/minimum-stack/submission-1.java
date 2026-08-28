class MinStack {
    public Stack<Integer> stack;
    private Stack<Integer> minStack;
   // public int min;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        // int min = minStack.isEmpty() ? val :
        //         Math.min(val,minStack.peek());
        // minStack.push(min);
        stack.push(val);
        if(minStack.isEmpty() || val <= minStack.peek()){
            minStack.push(val);
        }
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
        
    }
    
    public int top() {
        int top = stack.peek();
        return top;
    }
    
    public int getMin() {
        //this takes O(n)
        // int min = Collections.min(stack);
        return minStack.peek();
    }
}
