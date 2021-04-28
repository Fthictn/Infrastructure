
## CASE 2
**Version 1.0.0**

## Prerequisites
    #Docker engine

## Couchbase ve Docker teknolojileri kullanılarak veritabanı oluşturulması işlemlerini içermektedir.
<br/>

### 1.Veritabanının Yaratılması
<br/>

**1.1 Couchbase sunucuların ayağa kaldırılması**

`$ docker pull couchbase:community-6.6.0` containerlerin ayağa kaldırılmasında kullanılmak üzere 
Couchbase Image'in community-6.6.0 tagi lokale çekilir.

`$ docker compose up` hazırlanan docker-compose dosyası kullanılarak iki ayrı portta couchbase ayağa kaldırılır. 

**1.2 Veritabanının couchbase-cli kullanılarak oluşturulması**

`$ couchbase-cli cluster-init -c 127.0.0.1:8065 --cluster-username Administrator --cluster-password 123456 --services data,index,query --cluster-index-ramsize 256` 8065 portu üzerinde çalışacak cluster oluşturulur

`$ couchbase-cli server-add 127.0.0.1:8065 --username Administrator --password 123456 --server-add 172.17.0.3 --server-add-username Administrator --server-add-password 718293 --services data ` 172.17.0.3 adresinde çalışan ikinci node eklenir.

`$ couchbase-cli bucker-create --cluster 127.0.0.1:8065 --username Administrator --password 123456 --bucket employee --bucket-type couchbase --bucket-ramsize 100 --durability-min-level persistToMajority --enable-flush` employee adında bir bucket oluşturulur.

`$ couchbase-cli rebalance -c 127.0.0.1:8065 --username Administrator --password 123456` nodelar arasındaki rebalancing işlemi gerçekleştirilir.

**Not:** Couchbase cli komutları docker exec komutuyla kullanılabileceği gibi windows için **C:\Program Files\Couchbase\Server\bin>** dizini altında da çalıştırılabilir.

**1.3 Veritabanının couchbase-ui kullanılarak oluşturulması**

**1.3.1 Cluster oluşturulması** <br/>
Setup New Cluster butonuna tıklanarak açılan dialogda clusterle ilgili bilgiler girilir. <br/>
![cluster oluşturma](https://github.com/Fthictn/Nisan28/blob/main/CASE1/images/creatingdb/case1-8.png) <br/>
![cluster oluşturma](https://github.com/Fthictn/Nisan28/blob/main/CASE1/images/creatingdb/case1-9.png) <br/> <br/>

Bucket menüsü altında ADD BUCKET butonu ile bucket bilgileri girilerek Book adında bir bucket yaratılır. <br/>
![cluster oluşturma](https://github.com/Fthictn/Nisan28/blob/main/CASE1/images/creatingdb/case1-12.png) <br/> <br/>

Servers menüsü altında ADD SERVER butonu ile yeni node eklenir. <br/>
![cluster oluşturma](https://github.com/Fthictn/Nisan28/blob/main/CASE1/images/creatingdb/case1-10.png) <br/> <br/>

Servers menüsü altındaki Rebalance butonu ile rebalancing işlemi nodelar için uygulanır. <br/>
![cluster oluşturma](https://github.com/Fthictn/Nisan28/blob/main/CASE1/images/creatingdb/case1-11.png) <br/> <br/>
 
İki node üzeride rebalance işlemi uygulanmış veritabanı oluşturulmuş olur. <br/>
![cluster oluşturma](https://github.com/Fthictn/Nisan28/blob/main/CASE1/images/creatingdb/case1-14.png) <br/> <br/>


 








