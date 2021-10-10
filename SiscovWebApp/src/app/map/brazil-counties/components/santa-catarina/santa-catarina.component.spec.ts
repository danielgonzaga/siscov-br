import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SantaCatarinaComponent } from './santa-catarina.component';

describe('SantaCatarinaComponent', () => {
  let component: SantaCatarinaComponent;
  let fixture: ComponentFixture<SantaCatarinaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SantaCatarinaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SantaCatarinaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
