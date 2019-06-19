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
          title: 'Sobre nosotros',
          content: 'Somos un grupo de estudiantes de japonés de la Escuela de Idiomas de Málaga con nociones de programación y/o diseño gráfico. Decidimos hacer un proyecto para facilitar tanto a nosotros como al resto de estudiantes el estudio de kanjis.',
          link: 'Saber más',
          href: 'https://github.com/kabi404',
          icon: 'coffee'
        },
        {
          title: 'Software libre',
          content: 'El proyecto está protegido bajo una licencia de software MIT. Cualquier persona puede colaborar en el proyecto.',
          link: 'Ver licencia',
          href: 'https://github.com/kabi404/Kanjinary/blob/master/LICENSE',
          icon: 'unlock-alt'
        },
        {
          title: 'El proyecto',
          content: 'Todo el código y datos del proyecto está disponible en GitHub.',
          link: 'Ir al proyecto',
          href: 'https://github.com/kabi404/Kanjinary',
          icon: 'users'
        }
      ]
    }
  }
}
</script>
