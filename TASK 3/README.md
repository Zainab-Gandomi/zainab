package com.Scala.Task 3

object word_count {

  def main(args: Array[String]): Unit = {

    readFile()

  }
  def readFile(): Unit ={
    import scala.io.Source

    val filename = "C:\\Users\\zainab\\Desktop\\shakespeare.txt"
    var lines=""
    for (line <- Source.fromFile(filename).getLines){
      lines=lines+line
    }

    val str1=lines.toLowerCase   
    val word_counts = str1.filter(!_.isDigit)
    val word_split = word_counts.replaceAll("""[\p{Punct}&&[^.]]""", " ") //remove punchuation

    val count_split =word_split.split(" ")

    val wordCount = scala.collection.mutable.HashMap[String, Int]()

    for (word <- count_split) {
      val count = wordCount.getOrElse(word, 0)
      wordCount(word) = count + 1
    }
    println(wordCount)


  }

}
