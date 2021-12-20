1--Write a Scala program to count the number of occurrences of each element in a given list.


object Scala_List {    

  def list_elemnt_occurrences[A](list1:List[A]):Map[A, Int] = {
      list1.groupBy(el => el).map(e => (e._1, e._2.length))
    } 
    
    
    
    
2--  Write a Scala program to find the even and odd numbers from a given list.


object Scala_List
{
  def main(args: Array[String]): Unit = 
 {
   val nums = List(1, 2, 3, 4, 5, 7, 9, 10, 7 ,16, 11, 14, 12, 16)
   println("Original list:")
   println(nums)   
   val even_nums = nums.filter(_ % 2 ==0) 
   println("Even number of the said list:")
   println(even_nums)
   val odd_nums = nums.filter(_ % 2 != 0) 
   println("Odd number of the said list:")
   println(odd_nums)   
  }
}


3--Write a Scala program to remove duplicates from a given list.
    
object Scala_List
{
def main(args: Array[String]): Unit = 
 {
   val nums = List(1, 3, 5, 2, 7, 9, 11, 5, 2, 6, 8)
   println("Original list:")
   println(nums)   
   val result1 = nums.distinct
   println("Unique elements of the said list:")
   println(result1)
   val chars = List("a", "a", "b", "c", "d", "c", "e", "f", "g", "d")
   println("Original list:")
   println(chars)   
   val result2 = chars.distinct
   println("Unique elements of the said list:")
   println(result2)    
  }
}


4--Write a Scala program to find the largest and smallest number from a given list.


object Scala_List
{
def main(args: Array[String]): Unit = 
 {
   //Iterate over a list
   val nums = List(1, 3, 5,, 14, 12)
   println("Original list:")
   println(nums)   
   println("Largest number of the said list:")
   println(nums.max)
   println("Smallest number from the said list:")
   println(nums.min)
  }
}








