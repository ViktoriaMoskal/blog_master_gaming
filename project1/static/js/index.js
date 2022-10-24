        function showActivelink(menu) {
            try {
                let elem = document.getElementById(menu).querySelectorAll('a');
                let url = document.location.href
                for (const link of elem) {
                    if (link.href === url) {
                        link.classList.add('active')
                    }
                }
            } catch {
                console.log('error')
            }

        }
        showActivelink('menu')