import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.*;


class ChocolateDistribution {
    
    int n, m;
    int[] remainder_of_sum_upto;
    long[] sum_upto;
    int[] chocolates_in_hand;
    
    Map<Integer,Set<Integer>> remainders_map;
    
    
    public long sum_of_range(int start, int end) {
        
        if(start==end) return this.chocolates_in_hand[start];
        if(start==0) return this.sum_upto[end];
        return this.sum_upto[end]-this.sum_upto[start-1];
    }
    
    public long distribute_chocolates() {
        
        long max_sum = -1;
        for (Map.Entry<Integer,Set<Integer>> entry : this.remainders_map.entrySet()) {
            if (entry.getValue().size()!=0) {
                //System.out.print(entry.getKey());
                //System.out.println(entry.getValue().toString());
                if(entry.getKey()==0) {
                    int idx = Collections.max(entry.getValue());
                    //System.out.println("Max Direct : "+idx);
                    long sum = sum_of_range(0,idx);
                    if(sum>max_sum) max_sum = sum;
                    continue;
                }
                if(entry.getValue().size()>1) {
                int start = Collections.min(entry.getValue());
                int end = Collections.max(entry.getValue());
                long sum = sum_of_range(start+1,end);
                if(sum>max_sum) max_sum = sum;}
            }
        }
        if (max_sum!=-1) return max_sum/m;
        else return 0;
    }
    
    
    public ChocolateDistribution(int n, int[] chocolates_in_hand, int m) {
    
        this.n = n;
        this.m = m;
        this.sum_upto = new long[n];
        this.remainder_of_sum_upto = new int[n];
        this.chocolates_in_hand = chocolates_in_hand.clone();
        int sum = 0;
        long total_sum = 0;
        remainders_map = new HashMap<Integer, Set<Integer>>();
        
        for(int i=0; i<n; i++) {
            
            if (sum>=m) sum = sum%m;
            sum += chocolates_in_hand[i];
            total_sum += chocolates_in_hand[i];
            this.remainder_of_sum_upto[i] = sum%m;
            this.sum_upto[i] = total_sum;
            Set<Integer> mapped_set = remainders_map.get(this.remainder_of_sum_upto[i]); 
            if (mapped_set == null) {
                mapped_set = new HashSet<Integer>();
                remainders_map.put(this.remainder_of_sum_upto[i], mapped_set);
            }
            mapped_set.add(i);
        }
        
    }
    
    public static void main(String args[] ) throws Exception {
        Scanner s = new Scanner(System.in);
        //String name = s.nextLine();                 
        //System.out.println("");
        
        int num_test_cases = s.nextInt();
        
        for(int cnt=0; cnt<num_test_cases; cnt++) {
        int n = s.nextInt();
        int m = s.nextInt();
        int[] chocolates_in_hand = new int[n];
        
        for(int i=0; i<n; i++) chocolates_in_hand[i]=s.nextInt();
        
        ChocolateDistribution testObj = new ChocolateDistribution(n, chocolates_in_hand,m);
        //System.out.println(testObj.sum_upto[0]);
        //System.out.println(testObj.sum_upto[n-1]);
        
        //for(int i=0; i<n; i++) System.out.println(chocolates_in_hand[i]);
        
        System.out.println(testObj.distribute_chocolates());
        
        long max_sum = -1;
        //for(int i=0; i<n; i++) {
            long sum = 0;
            long max_sum_iteration = -1;
            //for(int j=i; j<n; j++) {
                //sum += chocolates_in_hand[j];
                //sum += testObj.sum_of_range(j);
                //sum = testObj.sum_of_range(i,j);
                //if(sum%m==0) if(sum>max_sum_iteration) max_sum_iteration = sum;
                
            //}
            //System.out.println(max_sum_iteration);
            if (max_sum_iteration>max_sum) max_sum = max_sum_iteration;
        //}
        
        //if (max_sum!=-1) System.out.println(max_sum/m);
        //else System.out.println("0");
    }
    }
}
