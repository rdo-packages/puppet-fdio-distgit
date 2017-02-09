%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-fdio
%global commit 9326e4237f4d161f297dc4493ab4928ea6e2bf0f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-fdio
Version:                0.0.1
Release:                1%{?alphatag}%{?dist}
Summary:                Puppet module for fdio projects
License:                ASL 2.0

URL:                    https://wiki.fd.io/view/Puppet-fdio

Source0:                https://github.com/radez/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib

Requires:               puppet >= 2.7.0

%description
Installs and configures FD.io projects like VPP and Honeycomb agent.

%prep
%setup -q -n %{name}-%{upstream_version}

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
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 0.0.1-1.9326e42git
- Ocata update 0.0.1 (9326e4237f4d161f297dc4493ab4928ea6e2bf0f)
