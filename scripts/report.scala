// animals with more than 1000 days in the shelter

//> using dep "org.mongodb:mongodb-driver-sync:5.1.0"

import com.mongodb.client.MongoClients
import com.mongodb.client.model.Filters

@main def run(): Unit =
  val client = MongoClients.create("mongodb://192.168.64.1:27017")
  val db = client.getDatabase("my-database")
  val collection = db.getCollection("animal_shelter")
  val filter = Filters.gt("days_in_shelter", 1000)
  val results = collection.find(filter)
  results.forEach(doc => println(doc.toJson()))
  client.close()