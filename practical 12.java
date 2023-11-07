package MongoDB;
import com.mongodb.*;
public class MongoDB {
public static void main(String[] args) {
MongoClient mongo=new MongoClient("localhost",27017);
System.out.println("Connected to the database successfully");
DB db=mongo.getDB("Info");
DBCollection table=db.createCollection("Personal",null);
BasicDBObject info1= new BasicDBObject();
info1.put("Name","Soham");
info1.put("Age", 20);
info1.put("Mobile Number","9912365723");
table.insert(info1);
BasicDBObject info2= new BasicDBObject();
info2.put("Name","Rohan");
info2.put("Age", 18);
info2.put("Mobile Number","78234109834");
table.insert(info2);
DBCursor cursor=table.find();
System.out.println("Insert Operation");
while(cursor.hasNext()) {
System.out.println(cursor.next());
}
System.out.println("Delete Operation");
table.remove(info1);
cursor=table.find();
while(cursor.hasNext()) {
System.out.println(cursor.next());
}
db.dropDatabase();
}
}
