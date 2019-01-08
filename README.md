# xml-to-yaml service
A RESTful service which awaits POST request at the 80 port, and responds with the same message converted to YAML format

The service is packed inside docker image which is build with gradle.

_Prerequisites:_**
```
Java JDK or JRE version >= 7
```

To build the Docker Image run:
```
./gradlew buildImage
```
The command calls the **buildImage** Gradle task and automatically uses Gradle v4.8 to build it. Pre-insalled Gradle v4.8 is not requiered. The Gradle wrapper will install it automatically if needed.

To run the service use command:
```
docker run -p 8080:80 [image_id]
```

Test curl request example:
```
curl -X POST -d '<xml><From>Jack</From><Body>Hello, it worked!</Body></xml>' 0.0.0.0:8080/xml/to/yaml/v1.0 -H "Content-Type: text/xml"
```

The service will send the message converted to YAML format.