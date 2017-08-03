%{?scl:%scl_package maven-reporting-api}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-reporting-api
Version:        3.0
Release:        11.2%{?dist}
# Maven-shared defines maven-reporting-api version as 3.0
Epoch:          1
Summary:        API to manage report generation
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-reporting-api
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-reporting-api-3.0 maven-reporting-api-3.0
# tar caf maven-reporting-api-3.0.tar.xz maven-reporting-api-3.0/
Source0:        %{pkg_name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.doxia:doxia-sink-api)

Provides:       %{?scl_prefix}maven-shared-reporting-api = %{epoch}:%{version}-%{release}

%description
API to manage report generation. Maven-reporting-api is included in Maven 2.x
core distribution, but moved to shared components to achieve report decoupling
from Maven 3 core.

This is a replacement package for maven-shared-reporting-api

%package javadoc
Summary:        Javadoc for %{pkg_name}
    

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q
cp %{SOURCE1} LICENSE.txt

%build
# Previous package provides groupIds org.apache.maven.shared and org.apache.maven.reporting
%mvn_alias : org.apache.maven.shared:maven-reporting-api
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{pkg_name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 1:3.0-11.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1:3.0-11.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-8
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:3.0-6
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-5
- Fix unowned directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-3
- Build with xmvn
- Resolves: rhbz#912437

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:3.0-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Tomas Radej <tradej@redhat.com> - 1:3.0-1
- Initial version
