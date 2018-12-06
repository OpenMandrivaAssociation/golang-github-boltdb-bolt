# http://github.com/boltdb/bolt
%global goipath         github.com/boltdb/bolt
Version:                1.3.1

%gometa

Name:           %{goname}
Release:        5%{?dist}
Summary:        A low-level key/value database for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%package -n boltdb
Summary:       %{summary}

%description -n boltdb
%{summary}

This package contains the bolt binary.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .


%build
%gobuildroot
%gobuild -o _bin/bolt %{goipath}/cmd/bolt

%install
%goinstall glide.lock glide.yaml
install -Dpm 0755 _bin/bolt %{buildroot}%{_bindir}/bolt

%check
# Takes too much time
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%files -n boltdb
%license LICENSE
%{_bindir}/bolt

%changelog
* Sat Nov 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.1-5
- Refresh SPEC

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.3.1-4.git2f1ce7a
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3.git2f1ce7a

- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.3.1-2.git2f1ce7a
- Upload glide.lock and glide.yaml

* Sun Mar 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.3.1-1.git2f1ce7a
- Update to v1.3.1

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.3.0-0.7.20160818git583e893
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.6.git583e893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.5.git583e893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.4.git583e893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-0.3.git583e893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 1.3.0-0.2.git583e893
- Polish the spec file
  related: #1246207

* Thu Sep 15 2016 jchaloup <jchaloup@redhat.com> - 1.3.0-0.1.git583e893
- Bump to upstream 583e8937c61f1af6513608ccc75c97b6abdf4ff9
  related: #1246207

* Mon Aug 01 2016 jchaloup <jchaloup@redhat.com> - 1.2.1-0.1.gitdfb2120
- Bump to upstream dfb21201d9270c1082d5fb0f07f500311ff72f18
  related: #1246207

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.2.gitc6ba97b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Mar 22 2016 jchaloup <jchaloup@redhat.com> - 1.2.0-0.1.gitc6ba97b
- Update to 1.2.0
- Polish spec file
  related: #1246207

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.git0b00eff
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.5.git0b00eff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 1.0-0.4.git0b00eff
- Bump to upstream 0b00effdd7a8270ebd91c24297e51643e370dd52
  related: #1246207

* Fri Sep 11 2015 jchaloup <jchaloup@redhat.com> - 1.0-0.3.git90fef38
- Bump to upstream 90fef389f98027ca55594edd7dbd6e7f3926fdad
  related: #1246207

* Thu Jul 30 2015 Fridolin Pokorny <fpokorny@redhat.com> - 1.0-0.2.git980670a
- Update of spec file to spec-2.0
  resolves: #1246207

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 1.0-0.1.git980670a
- Bump to upstream 980670afcebfd86727505b3061d8667195234816
  resolves: #1246207

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git3b44955
- First package for Fedora
  resolves: #1212099

