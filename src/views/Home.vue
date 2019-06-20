<template>
  <div class="home">

    <section class="container">
      <div class="columns">
        <div class="column has-text-centered m-t-lg m-b-lg">
          <h1 class="is-size-2">Sobre el proyecto</h1>
        </div>
      </div>

      <div class="columns is-multiline">
        <div v-for="(card, index) in cards" :key="index" class="column is-4">
          <IconCard
            v-bind:title="card.title"
            v-bind:content="card.content"
            v-bind:link="card.link"
            v-bind:href="card.href"
            v-bind:iconRef="card.icon"
          />
        </div>
      </div>
    </section>

    
  </div>
</template>

<script>
import IconCard from '@/components/IconCard.vue'

export default {
  name: 'home',

  components: {
    IconCard
  },

  data: function() {
    return {
      cards: [
        {
          title: 'Sobre mi',
          content: 'Soy un Ingeniero de Software y estudiante de japonés. Este proyecto está hecho para facilitar el estudio de kanjis mediante información y recursos.',
          link: 'Saber más',
          href: 'https://github.com/kabi404',
          icon: 'coffee'
        },
        {
          title: 'Software libre',
          content: 'El proyecto está protegido bajo la licencia de software libre MIT. Cualquier persona puede colaborar en el proyecto.',
          link: 'Ver licencia',
          href: 'https://github.com/kabi404/Kanjinary/blob/master/LICENSE',
          icon: 'unlock-alt'
        },
        {
          title: 'El proyecto',
          content: 'Todo el código y datos del proyecto está disponible en GitHub. Para participar tan sólo haz alguna modificación del código interesante o añade kanjis que aún no estén incluidos.',
          link: 'Ir al proyecto',
          href: 'https://github.com/kabi404/Kanjinary',
          icon: 'users'
        }
      ]
    }
  }
}
</script>
