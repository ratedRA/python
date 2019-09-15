Interface New1{
	Default void display();
}
class Check implements New1{
	public void display(){
		System.out.pritln("Done");
	}
	public static void main(String args[]){
		Check c = new Check()
		c.display()
	}
}