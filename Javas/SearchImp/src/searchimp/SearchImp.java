/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package searchimp;

/**
 *
 * @author chow
 * 
 */
import CITS2200.Graph;
import CITS2200.Search;
import java.util.Queue;

//getEdgeMatrix() (a graph method) must be implemented
//as well as get number of vertices to determine the array size (for the matrix I think)
public class SearchImp implements Search {
    public int[] getConnectedTree(Graph testGraph, int startVertex) {
        // TODO: Implement getConnectedTree.
	Queue<Integer> q = new Queue<>();
	q.offer(startVertex);
	int graphSize = testGraph.getNumberOfVertices();
	testGraph.
	
	while(!q.isEmpty()){
		q.remove()
	}
	testGraph.getEdgeMatrix()
	
		
	return null;
    }

    public int[] getDistances(Graph g, int startVertex) {
        // TODO: Implement getDistances.
	return null;
    }
    
    public int[][] getTimes(Graph g, int startVertex) {
        // TODO: Implement getTimes.
        return null;
    }
    public void dfs(){
	    
    }
}


