import java.util.Vector;
import java.util.Hashtable;
import java.util.Enumeration;
import java.io.*;

public class ReadNetwork
{
	//Command line arguments
	private static String graphFileName = "";

	// The adjacency matrix (similarity network)
	private static Hashtable AMatrix = new Hashtable(40000);
	
public static void main(String[] argv) throws FileNotFoundException, IOException
{
		
	// Get command line arguments
	if (argv != null) 
	{
		int len = argv.length;
		if (len == 1) 
		{
			graphFileName = argv[0];
		}
		else printUsage();
	}

	// read the graph file and create the adjacency matrix
    BufferedReader graphReader = new BufferedReader(new FileReader(graphFileName));

    String graphLine = graphReader.readLine(); // skip first line
	
	while (graphLine!=null)
	{
		String[] strs = split(graphLine,'\t');
		String p1 = strs[0];
		String p2 = strs[1];

		if (AMatrix.containsKey(p1))
		{
			Hashtable n = (Hashtable)(AMatrix.get(p1));
			n.put(p2,p2); // 1 means in complex with, 2 mean controls state change of
		}
		else
		{
			Hashtable n = new Hashtable(200);
			n.put(p2,p2);
			AMatrix.put(p1,n);	
		}

		if (AMatrix.containsKey(p2))
		{
			Hashtable n = (Hashtable)(AMatrix.get(p2));
			n.put(p1,p1);
		}
		else
		{
			Hashtable n = new Hashtable(200);
			n.put(p1,p1);
			AMatrix.put(p2,n);	
		}
				
		graphLine = graphReader.readLine();
	}


	System.out.println("There are "+AMatrix.size()+" nodes in the network.");

	int totalNumEdges = 0;
	int minDegree,maxDegree;
	String minD,maxD;
	minDegree = 90000;
	maxDegree = 0;
	minD = "";
	maxD = "";
	for (Enumeration en = AMatrix.keys();en.hasMoreElements();)
	{
		String p1 = (String)en.nextElement();
		Hashtable neighbors = (Hashtable)AMatrix.get(p1);
		if (neighbors.size()>maxDegree)
		{
			maxDegree = neighbors.size();
			maxD = p1;
		}
		if (neighbors.size()<minDegree)
		{
			minDegree = neighbors.size();
			minD = p1;
		}
		totalNumEdges = totalNumEdges + neighbors.size();	
	}

	System.out.println("Total number of edges = "+totalNumEdges);
	System.out.println("The average degree of the network is = "+(((float)totalNumEdges))/AMatrix.size());

	System.out.println("Protein with min degree = "+minD+" and it has "+minDegree+" edges.");	
	System.out.println("Protein with max degree = "+maxD+" and it has "+maxDegree+" edges.");	

}

	private static void printUsage()
	{
		System.out.println("Usage: java ReadNetwork <graph file name>");
		System.exit(1);
	}

	public static String[] split(String str, char delim)
    {
                // begin split
                Vector strsVec = new Vector(0,1);
                String tmp = str;
                while (tmp.indexOf(delim)!=-1)
                {
                		if (tmp.substring(0,tmp.indexOf(delim)).length()>0)
                        	strsVec.addElement(new String(tmp.substring(0,tmp.indexOf(delim))));
                        tmp = tmp.substring(tmp.indexOf(delim)+1,tmp.length());
                }
                strsVec.addElement(new String(tmp));
                String[] strs = new String[strsVec.capacity()];
                for (int s = 0; s < strsVec.capacity(); s++)
                        strs[s] = (String)strsVec.elementAt(s);
                // end of split
                return strs;
    }
}
