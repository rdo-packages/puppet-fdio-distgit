%{!?upstream_version: %global upstream_version %{commit}}
%global commit 6fd1c8e407eb57bcb42198975dd1fdb1c0de1013
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-fdio
Version:                18.01
Release:                3%{?alphatag}%{?dist}
Summary:                Puppet module for fdio projects
License:                ASL 2.0

URL:                    https://github.com/FDio/puppet-fdio

Source0:                https://github.com/FDio/puppet-fdio/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib

Requires:               puppet >= 2.7.0

%description
Installs and configures FD.io projects like VPP and Honeycomb agent.

%prep
%setup -q -n %{name}-%{shortcommit}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/fdio/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/fdio/



%files
%{_datadir}/openstack-puppet/modules/fdio/


%changelog
* Fri Apr 01 2022 RDO <dev@lists.rdoproject.org> 18.01-3.6fd1c8egit
- Update to post 18.01 (6fd1c8e407eb57bcb42198975dd1fdb1c0de1013)


