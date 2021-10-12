import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-santa-catarina',
  templateUrl: './santa-catarina.component.html',
  styleUrls: ['./santa-catarina.component.css']
})
export class SantaCatarinaComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
