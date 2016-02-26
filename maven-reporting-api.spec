%global pkg_name maven-reporting-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        3.0
Release:        5.12%{?dist}
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
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cp %{SOURCE1} LICENSE.txt
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
# Previous package provides groupIds org.apache.maven.shared and org.apache.maven.reporting
%mvn_alias : org.apache.maven.shared:maven-reporting-api
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt


%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 1:3.0-5.12
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1:3.0-5.11
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1:3.0-5.10
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-5.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-5.8
- Fix BR on maven-shared POM

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1:3.0-5.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1:3.0-5.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-5.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-5.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-5.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 1:3.0-5.3
- SCL-ize BR/R

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-5.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-5.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:3.0-5
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-4
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Feb 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:3.0-3
- Build with xmvn
- Resolves: rhbz#912437

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:3.0-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Tomas Radej <tradej@redhat.com> - 1:3.0-1
- Initial version

