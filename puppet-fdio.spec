%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppet-fdio
%global commit d9ad6d211b86111bdca6b78891808a1bbdec86d2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-fdio
Version:                0.0.1
Release:                2%{?alphatag}%{?dist}
Summary:                Puppet module for fdio projects
License:                ASL 2.0

URL:                    https://wiki.fd.io/view/Puppet-fdio

# XXX: since former github is not available anymore, tarball was generated manually
# from https://git.fd.io/puppet-fdio/
#  git archive --format=tar.gz -o puppet-fdio-d9ad6d2.tar.gz --prefix=puppet-fdio-d9ad6d211b86111bdca6b78891808a1bbdec86d2/ d9ad6d2
Source0:                https://hguemar.fedorapeople.org/openstack/%{upstream_name}-%{shortcommit}.tar.gz

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
* Fri Aug 25 2017 hguemar <hguemar@benihime.seireitei> - 0.0.1-2.d9ad6d2git
- Pike update 0.0.1 (d9ad6d211b86111bdca6b78891808a1bbdec86d2)


