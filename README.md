# xml-to-yaml service
A RESTful service which awaits POST request at the 80 port, and responds with the same message converted to YAML format

The service is packed inside docker image which is build with gradle.

Пример запроса для тестирования приложния:
curl -X POST -d '<xml><From>Jack</From><Body>Hello, it worked!</Body></xml>' 0.0.0.0:8080/xml/to/yaml/v1.0 -H "Content-Type: text/xml"


