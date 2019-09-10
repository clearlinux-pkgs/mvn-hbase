#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-hbase
Version  : 1.2.6
Release  : 5
URL      : https://github.com/apache/hbase/archive/rel/1.2.6.tar.gz
Source0  : https://github.com/apache/hbase/archive/rel/1.2.6.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-annotations/1.2.6/hbase-annotations-1.2.6-tests.jar
Source2  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-annotations/1.2.6/hbase-annotations-1.2.6.jar
Source3  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-annotations/1.2.6/hbase-annotations-1.2.6.pom
Source4  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-client/1.2.6/hbase-client-1.2.6.jar
Source5  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-client/1.2.6/hbase-client-1.2.6.pom
Source6  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-common/1.2.6/hbase-common-1.2.6-tests.jar
Source7  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-common/1.2.6/hbase-common-1.2.6.jar
Source8  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-common/1.2.6/hbase-common-1.2.6.pom
Source9  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop-compat/1.2.6/hbase-hadoop-compat-1.2.6-tests.jar
Source10  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop-compat/1.2.6/hbase-hadoop-compat-1.2.6.jar
Source11  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop-compat/1.2.6/hbase-hadoop-compat-1.2.6.pom
Source12  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop-compat/1.4.3/hbase-hadoop-compat-1.4.3-tests.jar
Source13  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop-compat/1.4.3/hbase-hadoop-compat-1.4.3.jar
Source14  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop-compat/1.4.3/hbase-hadoop-compat-1.4.3.pom
Source15  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop2-compat/1.2.6/hbase-hadoop2-compat-1.2.6-tests.jar
Source16  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop2-compat/1.2.6/hbase-hadoop2-compat-1.2.6.jar
Source17  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop2-compat/1.2.6/hbase-hadoop2-compat-1.2.6.pom
Source18  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop2-compat/1.4.3/hbase-hadoop2-compat-1.4.3-tests.jar
Source19  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop2-compat/1.4.3/hbase-hadoop2-compat-1.4.3.jar
Source20  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-hadoop2-compat/1.4.3/hbase-hadoop2-compat-1.4.3.pom
Source21  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-prefix-tree/1.2.6/hbase-prefix-tree-1.2.6.jar
Source22  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-prefix-tree/1.2.6/hbase-prefix-tree-1.2.6.pom
Source23  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-procedure/1.2.6/hbase-procedure-1.2.6.jar
Source24  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-procedure/1.2.6/hbase-procedure-1.2.6.pom
Source25  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-protocol/1.2.6/hbase-protocol-1.2.6.jar
Source26  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-protocol/1.2.6/hbase-protocol-1.2.6.pom
Source27  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-server/1.2.6/hbase-server-1.2.6-tests.jar
Source28  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-server/1.2.6/hbase-server-1.2.6.jar
Source29  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-server/1.2.6/hbase-server-1.2.6.pom
Source30  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-server/1.4.3/hbase-server-1.4.3-tests.jar
Source31  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-server/1.4.3/hbase-server-1.4.3.jar
Source32  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-server/1.4.3/hbase-server-1.4.3.pom
Source33  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-testing-util/1.2.6/hbase-testing-util-1.2.6.jar
Source34  : https://repo1.maven.org/maven2/org/apache/hbase/hbase-testing-util/1.2.6/hbase-testing-util-1.2.6.pom
Source35  : https://repo1.maven.org/maven2/org/apache/hbase/hbase/1.2.6/hbase-1.2.6.pom
Source36  : https://repo1.maven.org/maven2/org/apache/hbase/hbase/1.4.3/hbase-1.4.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 CC-BY-3.0 MIT
Requires: mvn-hbase-data = %{version}-%{release}
Requires: mvn-hbase-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-cmake
BuildRequires : buildreq-mvn

%description
Apache HBase [1] is an open-source, distributed, versioned, column-oriented
store modeled after Google' Bigtable: A Distributed Storage System for
Structured Data by Chang et al.[2]  Just as Bigtable leverages the distributed
data storage provided by the Google File System, HBase provides Bigtable-like
capabilities on top of Apache Hadoop [3].

%package data
Summary: data components for the mvn-hbase package.
Group: Data

%description data
data components for the mvn-hbase package.


%package license
Summary: license components for the mvn-hbase package.
Group: Default

%description license
license components for the mvn-hbase package.


%prep
%setup -q -n hbase-rel-1.2.6

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-hbase
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-hbase/LICENSE.txt
cp hbase-common/src/main/javadoc/META-INF/NOTICE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-common_src_main_javadoc_META-INF_NOTICE
cp hbase-common/src/test/resources/META-INF/NOTICE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-common_src_test_resources_META-INF_NOTICE
cp hbase-resource-bundle/src/main/resources/META-INF/LICENSE.vm %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-resource-bundle_src_main_resources_META-INF_LICENSE.vm
cp hbase-server/src/main/javadoc/META-INF/LICENSE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-server_src_main_javadoc_META-INF_LICENSE
cp hbase-server/src/main/javadoc/META-INF/NOTICE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-server_src_main_javadoc_META-INF_NOTICE
cp hbase-server/src/test/resources/META-INF/LICENSE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-server_src_test_resources_META-INF_LICENSE
cp hbase-server/src/test/resources/META-INF/NOTICE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-server_src_test_resources_META-INF_NOTICE
cp hbase-thrift/src/main/appended-resources/META-INF/LICENSE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_main_appended-resources_META-INF_LICENSE
cp hbase-thrift/src/main/appended-resources/META-INF/NOTICE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_main_appended-resources_META-INF_NOTICE
cp hbase-thrift/src/main/javadoc/META-INF/LICENSE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_main_javadoc_META-INF_LICENSE
cp hbase-thrift/src/main/javadoc/META-INF/NOTICE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_main_javadoc_META-INF_NOTICE
cp hbase-thrift/src/test/resources/META-INF/LICENSE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_test_resources_META-INF_LICENSE
cp hbase-thrift/src/test/resources/META-INF/NOTICE %{buildroot}/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_test_resources_META-INF_NOTICE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-annotations/1.2.6
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-annotations/1.2.6/hbase-annotations-1.2.6-tests.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-annotations/1.2.6
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-annotations/1.2.6/hbase-annotations-1.2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-annotations/1.2.6
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-annotations/1.2.6/hbase-annotations-1.2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-client/1.2.6
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-client/1.2.6/hbase-client-1.2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-client/1.2.6
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-client/1.2.6/hbase-client-1.2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-common/1.2.6
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-common/1.2.6/hbase-common-1.2.6-tests.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-common/1.2.6
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-common/1.2.6/hbase-common-1.2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-common/1.2.6
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-common/1.2.6/hbase-common-1.2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.2.6
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.2.6/hbase-hadoop-compat-1.2.6-tests.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.2.6
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.2.6/hbase-hadoop-compat-1.2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.2.6
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.2.6/hbase-hadoop-compat-1.2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.4.3
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.4.3/hbase-hadoop-compat-1.4.3-tests.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.4.3
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.4.3/hbase-hadoop-compat-1.4.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.4.3
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.4.3/hbase-hadoop-compat-1.4.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.2.6
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.2.6/hbase-hadoop2-compat-1.2.6-tests.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.2.6
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.2.6/hbase-hadoop2-compat-1.2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.2.6
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.2.6/hbase-hadoop2-compat-1.2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.4.3
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.4.3/hbase-hadoop2-compat-1.4.3-tests.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.4.3
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.4.3/hbase-hadoop2-compat-1.4.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.4.3
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.4.3/hbase-hadoop2-compat-1.4.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-prefix-tree/1.2.6
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-prefix-tree/1.2.6/hbase-prefix-tree-1.2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-prefix-tree/1.2.6
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-prefix-tree/1.2.6/hbase-prefix-tree-1.2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-procedure/1.2.6
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-procedure/1.2.6/hbase-procedure-1.2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-procedure/1.2.6
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-procedure/1.2.6/hbase-procedure-1.2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-protocol/1.2.6
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-protocol/1.2.6/hbase-protocol-1.2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-protocol/1.2.6
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-protocol/1.2.6/hbase-protocol-1.2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.2.6
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.2.6/hbase-server-1.2.6-tests.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.2.6
cp %{SOURCE28} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.2.6/hbase-server-1.2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.2.6
cp %{SOURCE29} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.2.6/hbase-server-1.2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.4.3
cp %{SOURCE30} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.4.3/hbase-server-1.4.3-tests.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.4.3
cp %{SOURCE31} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.4.3/hbase-server-1.4.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.4.3
cp %{SOURCE32} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.4.3/hbase-server-1.4.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-testing-util/1.2.6
cp %{SOURCE33} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-testing-util/1.2.6/hbase-testing-util-1.2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-testing-util/1.2.6
cp %{SOURCE34} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase-testing-util/1.2.6/hbase-testing-util-1.2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase/1.2.6
cp %{SOURCE35} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase/1.2.6/hbase-1.2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase/1.4.3
cp %{SOURCE36} %{buildroot}/usr/share/java/.m2/repository/org/apache/hbase/hbase/1.4.3/hbase-1.4.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/hbase/hbase-annotations/1.2.6/hbase-annotations-1.2.6-tests.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-annotations/1.2.6/hbase-annotations-1.2.6.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-annotations/1.2.6/hbase-annotations-1.2.6.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-client/1.2.6/hbase-client-1.2.6.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-client/1.2.6/hbase-client-1.2.6.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-common/1.2.6/hbase-common-1.2.6-tests.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-common/1.2.6/hbase-common-1.2.6.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-common/1.2.6/hbase-common-1.2.6.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.2.6/hbase-hadoop-compat-1.2.6-tests.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.2.6/hbase-hadoop-compat-1.2.6.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.2.6/hbase-hadoop-compat-1.2.6.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.4.3/hbase-hadoop-compat-1.4.3-tests.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.4.3/hbase-hadoop-compat-1.4.3.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop-compat/1.4.3/hbase-hadoop-compat-1.4.3.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.2.6/hbase-hadoop2-compat-1.2.6-tests.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.2.6/hbase-hadoop2-compat-1.2.6.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.2.6/hbase-hadoop2-compat-1.2.6.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.4.3/hbase-hadoop2-compat-1.4.3-tests.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.4.3/hbase-hadoop2-compat-1.4.3.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-hadoop2-compat/1.4.3/hbase-hadoop2-compat-1.4.3.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-prefix-tree/1.2.6/hbase-prefix-tree-1.2.6.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-prefix-tree/1.2.6/hbase-prefix-tree-1.2.6.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-procedure/1.2.6/hbase-procedure-1.2.6.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-procedure/1.2.6/hbase-procedure-1.2.6.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-protocol/1.2.6/hbase-protocol-1.2.6.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-protocol/1.2.6/hbase-protocol-1.2.6.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.2.6/hbase-server-1.2.6-tests.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.2.6/hbase-server-1.2.6.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.2.6/hbase-server-1.2.6.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.4.3/hbase-server-1.4.3-tests.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.4.3/hbase-server-1.4.3.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-server/1.4.3/hbase-server-1.4.3.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase-testing-util/1.2.6/hbase-testing-util-1.2.6.jar
/usr/share/java/.m2/repository/org/apache/hbase/hbase-testing-util/1.2.6/hbase-testing-util-1.2.6.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase/1.2.6/hbase-1.2.6.pom
/usr/share/java/.m2/repository/org/apache/hbase/hbase/1.4.3/hbase-1.4.3.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-hbase/LICENSE.txt
/usr/share/package-licenses/mvn-hbase/hbase-common_src_main_javadoc_META-INF_NOTICE
/usr/share/package-licenses/mvn-hbase/hbase-common_src_test_resources_META-INF_NOTICE
/usr/share/package-licenses/mvn-hbase/hbase-resource-bundle_src_main_resources_META-INF_LICENSE.vm
/usr/share/package-licenses/mvn-hbase/hbase-server_src_main_javadoc_META-INF_LICENSE
/usr/share/package-licenses/mvn-hbase/hbase-server_src_main_javadoc_META-INF_NOTICE
/usr/share/package-licenses/mvn-hbase/hbase-server_src_test_resources_META-INF_LICENSE
/usr/share/package-licenses/mvn-hbase/hbase-server_src_test_resources_META-INF_NOTICE
/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_main_appended-resources_META-INF_LICENSE
/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_main_appended-resources_META-INF_NOTICE
/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_main_javadoc_META-INF_LICENSE
/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_main_javadoc_META-INF_NOTICE
/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_test_resources_META-INF_LICENSE
/usr/share/package-licenses/mvn-hbase/hbase-thrift_src_test_resources_META-INF_NOTICE
